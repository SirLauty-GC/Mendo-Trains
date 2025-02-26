import pygame
import VarGlob

class Boton_via_bifurcada(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        if VarGlob.modo_const_rotada == 0:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_false.png")
            if VarGlob.modo_const_via_bifurcada == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 1:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_arr.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_arr_false.png")
            if VarGlob.modo_const_via_bifurcada == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 2:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_izq.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_izq_false.png")
            if VarGlob.modo_const_via_bifurcada == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 3:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_abj.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/bifurcada/icono_via_bifurcada_rotada_abj_false.png")
            if VarGlob.modo_const_via_bifurcada == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))