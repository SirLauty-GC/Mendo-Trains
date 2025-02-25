import pygame

class Tren:
    def __init__(self, nombre, velocidad, vagones, capacidad, x, y, width, height, sprite=None):
        self.nombre = nombre
        self.velocidad = velocidad
        self.vagones = vagones
        self.capacidad = capacidad
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = sprite

    def definirSprite(self, sprite):
        self.sprite = pygame.image.load(sprite).convert()

pygame.init()
