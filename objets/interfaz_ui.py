import pygame
import VarGlob
from objets.interfaz.boton_construccion import Boton_constr
from objets.interfaz.boton_via_recta import Boton_via_recta
from objets.interfaz.boton_via_codo import Boton_via_codo
from objets.interfaz.boton_via_bifurcada import Boton_via_bifurcada
from objets.interfaz.boton_demolicion import Boton_demol
from objets.interfaz.boton_vacio import Boton_vacio

class Interfaz:
    def __init__(self):
        self.sprite_boton_uno = pygame.sprite.GroupSingle()
        self.sprite_boton_dos = pygame.sprite.GroupSingle()
        self.sprite_boton_tres = pygame.sprite.GroupSingle()
        self.sprite_boton_cuatro = pygame.sprite.GroupSingle()
        self.sprite_boton_cinco = pygame.sprite.GroupSingle()
        self.sprite_boton_seis = pygame.sprite.GroupSingle()
        self.sprite_boton_siete = pygame.sprite.GroupSingle()
        self.sprite_boton_ocho = pygame.sprite.GroupSingle()
        self.screen = pygame.display.get_surface()
        self.Panel = pygame.image.load("./sprites/ui/panel.png")
        self.x = 8
        self.y = (VarGlob.alto_pantalla - 610) // 2
        self.crear_panel()
    
    def crear_panel(self):
        self.screen.blit(self.Panel,(self.x, self.y))
        self.crear_botones()
    
    def crear_botones(self):
        botones_ubicacion = {
            1 : (self.screen, self.x + 16, self.y + 10, self.sprite_boton_uno),
            2 : (self.screen, self.x + 16, self.y + 84, self.sprite_boton_dos),
            3 : (self.screen, self.x + 16, self.y + 158, self.sprite_boton_tres),
            4 : (self.screen, self.x + 16, self.y + 232, self.sprite_boton_cuatro),
            5 : (self.screen, self.x + 16, self.y + 306, self.sprite_boton_cinco),
            6 : (self.screen, self.x + 16, self.y + 380, self.sprite_boton_seis),
            7 : (self.screen, self.x + 16, self.y + 454, self.sprite_boton_siete),
            8 : (self.screen, self.x + 16, self.y + 528, self.sprite_boton_ocho)
        }
        if VarGlob.modo_construccion == False & VarGlob.modo_demolicion == False:
            Boton_constr(*botones_ubicacion[1])
            Boton_demol(*botones_ubicacion[2])

        for i in range(3,9,1):
            Boton_vacio(*botones_ubicacion[i])

        if VarGlob.modo_construccion:
            Boton_constr(*botones_ubicacion[1])
            Boton_via_recta(*botones_ubicacion[2])
            Boton_via_codo(*botones_ubicacion[3])
            Boton_via_bifurcada(*botones_ubicacion[4])