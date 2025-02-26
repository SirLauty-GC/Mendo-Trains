import pygame 
class Via_recta(pygame.sprite.Sprite):
    def __init__(self, pos, groups, rot):
        super().__init__(groups)

        self.image = pygame.image.load("./sprites/vias/via_recta.png")
        if rot == 1:
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(topleft = pos)
