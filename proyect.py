import pygame, sys
import VarGlob
from objets.nivel import Nivel
from objets.interfaz_ui import Interfaz

pygame.init()

# Configuración de pantalla
limite_pantalla = 48
velocidad_camara = 8

pygame.display.set_caption("Trenes")

screen = pygame.display.set_mode((VarGlob.ancho_pantalla, VarGlob.alto_pantalla))
clock = pygame.time.Clock()

class Juego:
    def __init__(self):
        self.nivel = Nivel()

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        VarGlob.modo_construccion = not VarGlob.modo_construccion
                        VarGlob.modo_demolicion, VarGlob.modo_const_via_recta, VarGlob.modo_const_via_codo, VarGlob.modo_const_via_bifurcada = False, False, False, False

                    if event.key == pygame.K_1:
                        if VarGlob.modo_construccion == True:
                            VarGlob.modo_const_via_recta = not VarGlob.modo_const_via_recta
                            VarGlob.modo_const_via_codo, VarGlob.modo_const_via_bifurcada = False, False
                    if event.key == pygame.K_2:
                        if VarGlob.modo_construccion == True:
                            VarGlob.modo_const_via_codo = not VarGlob.modo_const_via_codo
                            VarGlob.modo_const_via_recta, VarGlob.modo_const_via_bifurcada = False, False
                    if event.key == pygame.K_3:
                        if VarGlob.modo_construccion == True:
                            VarGlob.modo_const_via_bifurcada = not VarGlob.modo_const_via_bifurcada
                            VarGlob.modo_const_via_recta, VarGlob.modo_const_via_codo = False, False

                    if event.key == pygame.K_w:
                        if VarGlob.modo_construccion == False:
                            VarGlob.modo_demolicion = not VarGlob.modo_demolicion
                    
                    if event.key == pygame.K_t:
                        VarGlob.offset_x = 0
                        VarGlob.offset_y = 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    if VarGlob.modo_construccion == True:
                        if event.button == 1:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            tile = self.nivel.detectar_tile(mouse_x, mouse_y, VarGlob.offset_x, VarGlob.offset_y)
                            tile_vias = self.nivel.detectar_via(mouse_x, mouse_y, VarGlob.offset_x, VarGlob.offset_y)
                            if tile:
                                if tile_vias[0] == '':
                                    self.nivel.construir_via(tile)
                        
                    if VarGlob.modo_demolicion == True:
                        if event.button == 1:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            tile = self.nivel.detectar_via(mouse_x, mouse_y, VarGlob.offset_x, VarGlob.offset_y)
                            if tile:
                                self.nivel.desstruir_via(tile)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if mouse_x < limite_pantalla:  # Izquierda
                if VarGlob.offset_x < 0:
                    VarGlob.offset_x += velocidad_camara
            if mouse_x > VarGlob.ancho_pantalla - limite_pantalla:  # Derecha
                if VarGlob.offset_x > VarGlob.ancho_pantalla - VarGlob.ancho_mundo:
                    VarGlob.offset_x -= velocidad_camara
            if mouse_y < limite_pantalla:  # Arriba
                if VarGlob.offset_y < 0:
                    VarGlob.offset_y += velocidad_camara
            if mouse_y > VarGlob.alto_pantalla - limite_pantalla:  # Abajo
                if VarGlob.offset_y > VarGlob.alto_pantalla - VarGlob.alto_mundo:
                    VarGlob.offset_y -= velocidad_camara
            
            screen.fill("black")

            self.nivel.movimiento_camara(VarGlob.offset_x, VarGlob.offset_y)
            
            self.interfaz = Interfaz()

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.corre_juego()
