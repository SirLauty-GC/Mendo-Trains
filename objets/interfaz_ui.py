import pygame
import VarGlob
from objets.interfaz.boton_construccion import Boton_constr
from objets.interfaz.boton_demolicion import Boton_demol

class Interfaz:
    def __init__(self):
        self.sprites_interfaz_ui = pygame.sprite.Group()
        self.screen = pygame.display.get_surface()
        self.Panel = pygame.image.load("./sprites/ui/panel.png")
        self.x = 8
        self.y = (VarGlob.alto_pantalla - 300) // 2
        self.crear_panel()
    
    def crear_panel(self):
        self.screen.blit(self.Panel,(self.x, self.y))
        self.crear_botones()
    
    def crear_botones(self):
        # Construccion
        Boton_constr(self.screen, self.x + 16, self.y + 10)
        # Demolicion
        Boton_demol(self.screen, self.x + 16, self.y + 74)