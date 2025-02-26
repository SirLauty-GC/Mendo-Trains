import pygame
import VarGlob

class Boton_via_recta(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        if VarGlob.modo_const_rotada == 0 or VarGlob.modo_const_rotada == 2:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/recta/icono_via_recta.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/recta/icono_via_recta_false.png")
            if VarGlob.modo_const_via_recta == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))
        elif VarGlob.modo_const_rotada == 1 or VarGlob.modo_const_rotada == 3:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/recta/icono_via_recta_rotada.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/recta/icono_via_recta_rotada_false.png")
            if VarGlob.modo_const_via_recta == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))