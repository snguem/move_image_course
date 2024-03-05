# on import le module(la boite a outils) pygame
import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, rect:pygame.rect.Rect) -> None:
        super().__init__()
        # chargement de l'image
        #   "Image1.png" = chemin relatif de l'image
        self.image = pygame.image.load("img/Image1.png")
        # redimenssionnement de l'image
        #   largeur = 150
        #   hauteur = 150
        self.image = pygame.transform.scale(self.image, (150, 150))
        # on recupere le rectangle associe a l'image
        self.rect = self.image.get_rect()
        # on lui donne une position d'origine
        self.rect.center = rect.center
