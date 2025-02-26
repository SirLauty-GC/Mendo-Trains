import pygame
import VarGlob

class Boton_constr_rotar(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group):
        super().__init__(group)
        icono = pygame.image.load("./sprites/ui/icono_constr_rotar.png")
        screen.blit(icono,(x, y))