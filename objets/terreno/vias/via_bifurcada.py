import pygame 
class Via_bifurcada(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/vias/via_bifurcada.png")
        self.rect = self.image.get_rect(topleft = pos)
