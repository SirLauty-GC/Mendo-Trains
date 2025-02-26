import pygame 
class Via_bifurcada(pygame.sprite.Sprite):
    def __init__(self, pos, groups, rot):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/vias/via_bifurcada.png")
        if rot > 1:
            self.image = pygame.transform.rotate(self.image, rot * 90)
        self.rect = self.image.get_rect(topleft = pos)
