import pygame
import VarGlob

class Boton_demol(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        icono_true = pygame.image.load("./sprites/ui/icono_demolicion.png")
        icono_false = pygame.image.load("./sprites/ui/icono_demolicion_false.png")
        if VarGlob.modo_demolicion == True:
            screen.blit(icono_true,(x, y))
        else:
            screen.blit(icono_false,(x, y))