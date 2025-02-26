import pygame
import VarGlob

class Boton_via_codo(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        if VarGlob.modo_const_rotada == 0:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_false.png")
            if VarGlob.modo_const_via_codo == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 1:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_arr_der.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_arr_der_false.png")
            if VarGlob.modo_const_via_codo == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 2:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_izq_arr.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_izq_arr_false.png")
            if VarGlob.modo_const_via_codo == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))

        if VarGlob.modo_const_rotada == 3:
            icono_true = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_izq_abj.png")
            icono_false = pygame.image.load("./sprites/ui/iconos_vias/codo/icono_via_codo_rotada_izq_abj_false.png")
            if VarGlob.modo_const_via_codo == True:
                screen.blit(icono_true,(x, y))
            else:
                screen.blit(icono_false,(x, y))