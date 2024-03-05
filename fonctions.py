from classes import (Object, pygame)

def deplacement(deplacements:list) -> list:
    # recuperation de tous les bouttons presses
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        # on se deplace vers le haut
        deplacements[1] = -10
    elif key[pygame.K_DOWN]:
        # on se deplace vers le bas
        deplacements[1] = 10
    elif key[pygame.K_LEFT]:
        # on se deplace vers la gauche
        deplacements[0] = -10
    elif key[pygame.K_RIGHT]:
        # on se deplace vers la droite
        deplacements[0] = 10
    # 
    return deplacements
    

def initialisation(rect:pygame.rect.Rect) -> tuple:
    # on cree une instance de la classe Object
    object_ = Object(rect)
    # on cree le groupe
    object_sprite = pygame.sprite.GroupSingle(object_)
    # 
    return object_, object_sprite

def initialisation_ecran() -> pygame.Surface:
    # on cree l'ecran avec les dimension :
    #   largeur : 800
    #   hauteur : 600
    ecran = pygame.display.set_mode((800, 600))
    # le titre du jeu
    pygame.display.set_caption(f"deplacer une image")
    # 
    return ecran
    