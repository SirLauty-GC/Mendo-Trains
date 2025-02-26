import pygame
import VarGlob

class Boton_vacio(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        icono = pygame.image.load("./sprites/ui/icono_vacio.png")
        screen.blit(icono,(x, y))