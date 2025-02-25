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
            pass
        else:
            tile_x = tile[1] * 32
            tile_y = tile[2] * 32
            tile = Via((tile_x, tile_y), [self.sprites_de_fondo, self.obstaculo])

    def desstruir_via(self, tile):
        tile_x = tile[1] * 32
        tile_y = tile[2] * 32
        Via.remove