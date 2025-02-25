import pygame
import csv
import numpy as np
from objets.terreno.mar import Mar
from objets.terreno.montana import Montana
from objets.terreno.colina import Colina
from objets.terreno.arena import Arena
from objets.terreno.pasto import Pasto
from objets.terreno.via import Via

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
    
    def cargar_partida(self):
        tipos_tile= {
            "v": Via
        }
        for row_index_r, row in enumerate(self.partida_guardada):
            for col_index_r, col in enumerate(row):
                if col in tipos_tile:
                    x = col_index_r * 32
                    y = row_index_r * 32
                    tipos_tile[col]((x, y), [self.sprites_de_fondo, self.obstaculo])

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
    
    def construir_via(self, tile):
        if tile[0] == 'a':
            return
        fila, columna = tile[1], tile[2]
        tile_x, tile_y = fila * 32, columna * 32
        tile = Via((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo])
        self.partida_guardada[columna][fila] = "v"
        self.guardar_mapa_csv("partida_guardada.csv")  
        if self.partida_guardada[columna][fila] == "v":
            print("hecho bro")

    def guardar_mapa_csv(self, archivo_csv):
        ruta_completa = f"./partidas/{archivo_csv}"
        with open(ruta_completa, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.partida_guardada)
    
    def detectar_via(self, mouse_x, mouse_y, offset_x, offset_y):
        global_x = mouse_x - offset_x
        global_y = mouse_y - offset_y

        tile_x = global_x // 32
        tile_y = global_y // 32

        if 0 <= tile_y < len(self.partida_guardada) and 0 <= tile_x < len(self.partida_guardada[0]):
            print(self.partida_guardada[tile_y][tile_x], tile_x, tile_y)
            return self.partida_guardada[tile_y][tile_x], tile_x, tile_y
        return None

    def desstruir_via(self, tile):
        if tile[0] == 'v':
            print("Vía a destruir waawa")
            fila, columna = tile[1], tile[2]
            self.partida_guardada[columna][fila] = ""
            self.guardar_mapa_csv("partida_guardada.csv")  
            if self.partida_guardada[columna][fila] == "":
                print("hecho bro")
            for sprite in self.obstaculo:
                if isinstance(sprite, Via) and sprite.rect.topleft == (fila * 32, columna * 32):
                    sprite.kill()