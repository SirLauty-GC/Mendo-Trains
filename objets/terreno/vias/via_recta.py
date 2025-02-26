import pygame 
class Via_recta(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/vias/via_recta.png")
        self.rect = self.image.get_rect(topleft = pos)
