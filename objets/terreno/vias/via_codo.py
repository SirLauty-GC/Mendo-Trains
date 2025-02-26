import pygame 
class Via_codo(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/vias/via_codo.png")
        self.rect = self.image.get_rect(topleft = pos)
