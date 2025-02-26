import pygame
import VarGlob

class Boton_via_codo(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        icono_true = pygame.image.load("./sprites/ui/icono_via_codo.png")
        icono_false = pygame.image.load("./sprites/ui/icono_via_codo_false.png")
        if VarGlob.modo_const_via_codo == True:
            screen.blit(icono_true,(x, y))
        else:
            screen.blit(icono_false,(x, y))