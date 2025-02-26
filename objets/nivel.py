import pygame
import csv
import numpy as np
import VarGlob
from objets.terreno.mar import Mar
from objets.terreno.montana import Montana
from objets.terreno.colina import Colina
from objets.terreno.arena import Arena
from objets.terreno.pasto import Pasto
from objets.terreno.vias.via_recta import Via_recta
from objets.terreno.vias.via_codo import Via_codo
from objets.terreno.vias.via_bifurcada import Via_bifurcada

def leer_mapa(ruta):
    with open(ruta, newline='') as archivo:
        reader = csv.reader(archivo)
        return [list(row) for row in reader]

class Nivel:
    def __init__(self):
        self.mapa = leer_mapa("./objets/mapa-cuyo.csv")
        self.partida_guardada = np.array(leer_mapa("./partidas/partida_guardada.csv"))
        self.screen = pygame.display.get_surface()
        self.sprites_de_fondo = pygame.sprite.Group()
        self.obstaculo = pygame.sprite.Group()

        self.crear_mapa()
        self.cargar_partida()
    
    def crear_mapa(self):
        tipos_terreno= {
            "a": Mar,
            "m": Montana,
            "c": Colina,
            "s": Arena,
            "l": Pasto
        }
        for row_index_r, row in enumerate(self.mapa):
            for col_index_r, col in enumerate(row):
                if col in tipos_terreno:
                    x = col_index_r * 32
                    y = row_index_r * 32
                    tipos_terreno[col]((x, y), [self.sprites_de_fondo, self.obstaculo])
        VarGlob.ancho_mundo = (col_index_r + 1) * 32
        VarGlob.alto_mundo = (row_index_r + 1) * 32
        
    
    def cargar_partida(self):
        tipos_tile= {
            "a": [Via_recta, 0],
            "b": [Via_recta, 1],
            "c": [Via_codo, 0],
            "d": [Via_codo, 1],
            "e": [Via_codo, 2],
            "f": [Via_codo, 3],
            "g": [Via_bifurcada, 0],
            "h": [Via_bifurcada, 1],
            "i": [Via_bifurcada, 2],
            "j": [Via_bifurcada, 3]
        }
        for row_index_r, row in enumerate(self.partida_guardada):
            for col_index_r, col in enumerate(row):
                if col in tipos_tile:
                    x = col_index_r * 32
                    y = row_index_r * 32
                    clase_tile, rot = tipos_tile[col]
                    clase_tile((x, y), [self.sprites_de_fondo, self.obstaculo],rot)
                    print(rot)

    def movimiento_camara(self, offset_x=0, offset_y=0):
        self.sprites_de_fondo.update()
        for sprite in self.sprites_de_fondo:
            self.screen.blit(sprite.image, (sprite.rect.x + offset_x, sprite.rect.y + offset_y))
    
    def detectar_tile(self, mouse_x, mouse_y, offset_x, offset_y):
        global_x = mouse_x - offset_x
        global_y = mouse_y - offset_y

        tile_x = global_x // 32
        tile_y = global_y // 32

        if 0 <= tile_y < len(self.mapa) and 0 <= tile_x < len(self.mapa[0]):
            return self.mapa[tile_y][tile_x], tile_x, tile_y
        return None
    
    def detectar_via(self, mouse_x, mouse_y, offset_x, offset_y):
        global_x = mouse_x - offset_x
        global_y = mouse_y - offset_y

        tile_x = global_x // 32
        tile_y = global_y // 32

        if 0 <= tile_y < len(self.partida_guardada) and 0 <= tile_x < len(self.partida_guardada[0]):
            return self.partida_guardada[tile_y][tile_x], tile_x, tile_y
        return None
    
    def construir_via(self, tile):
        if tile[0] == 'a':
            return
        fila, columna = tile[1], tile[2]
        tile_x, tile_y = fila * 32, columna * 32
        rot = VarGlob.modo_const_rotada
        if VarGlob.modo_const_via_recta == True: # Vía recta
            if rot == 0 or rot == 2:
                tile = Via_recta((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo], 0)
                self.partida_guardada[columna][fila] = "a"
            if rot == 1 or rot == 3:
                tile = Via_recta((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo], 1)
                self.partida_guardada[columna][fila] = "b"

        if VarGlob.modo_const_via_codo == True: # Vía codo
            tile = Via_codo((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo], rot)
            if rot == 0:
                self.partida_guardada[columna][fila] = "c"
            elif rot == 1:
                self.partida_guardada[columna][fila] = "d"
            elif rot == 2:
                self.partida_guardada[columna][fila] = "e"
            elif rot == 3:
                self.partida_guardada[columna][fila] = "f"

        if VarGlob.modo_const_via_bifurcada == True:
            tile = Via_bifurcada((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo], rot)
            if rot == 0:
                self.partida_guardada[columna][fila] = "g"
            elif rot == 1:
                self.partida_guardada[columna][fila] = "h"
            elif rot == 2:
                self.partida_guardada[columna][fila] = "i"
            elif rot == 3:
                self.partida_guardada[columna][fila] = "j"

        self.guardar_mapa_csv("partida_guardada.csv")

    def guardar_mapa_csv(self, archivo_csv):
        ruta_completa = f"./partidas/{archivo_csv}"
        with open(ruta_completa, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.partida_guardada)

    def desstruir_via(self, tile):
        if tile[0] != "":
            fila, columna = tile[1], tile[2]
            self.partida_guardada[columna][fila] = ""
            self.guardar_mapa_csv("partida_guardada.csv")
            tipo_tile = [Via_recta, Via_codo, Via_bifurcada]
            for i in range(0,3,1):
                for sprite in self.obstaculo:
                    if isinstance(sprite, tipo_tile[i]) and sprite.rect.topleft == (fila * 32, columna * 32):
                        sprite.kill()