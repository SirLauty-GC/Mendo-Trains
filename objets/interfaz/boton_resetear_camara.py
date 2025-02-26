import pygame
import VarGlob

class Boton_resetear_camara(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        icono = pygame.image.load("./sprites/ui/icono_resetear_camara.png")
        screen.blit(icono,(x, y))