import pygame
class Estacion(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/estacion.png")
        self.rect = self.image.get_rect(topleft = pos)