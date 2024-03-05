from fonctions import *

# 
ecran = initialisation_ecran()
# 
object_, object_sprite = initialisation(ecran.get_rect())
# la variable qui maintien le jeu actif
game = True
# la boucle principale du jeu
while game:
    # on efface l'ecran
    ecran.fill("black")
    # la boucle qui gere les evenements utilisateur
    for event in pygame.event.get():
        # on teste si l'evenement est de quitter|fermer l'ecran du jeu
        if event.type == pygame.QUIT:
            # on annule la variable qui maintien le jeu
            game = False
    
    # les deplacements de l'image
    deplacements = deplacement([0,0])
    # on fait deplacer l'image 
    
    for object in object_sprite:
        object.rect.centerx += deplacements[0]
        object.rect.centery += deplacements[1]
            
    # on affiche les elements du groupe
    object_sprite.draw(ecran)
    # on fait la mise a jour de l'ecran
    pygame.display.flip()
    # on definit le nombre de fps
    pygame.time.Clock().tick(60)
            

# on ferme la boite(le module)
pygame.quit()

