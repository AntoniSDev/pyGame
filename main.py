import pygame
pygame.init()

# générer la fenêtre du jeu
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

running = True

# boucle while running true
while running:

    # appliquer arrière plan du jeu
    screen.blit(background, (0, -200))

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
