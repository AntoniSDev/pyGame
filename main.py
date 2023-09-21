import pygame
import math
from game import Game

pygame.init()

# générer la fenêtre du jeu
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

# importer notre banière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer le bouton start
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle while running true
while running:

    # appliquer arrière plan du jeu
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé
    if game.is_playing:
        # déclencher les instruction de la partie
        game.update(screen)
    # vérifier si le jeu n'a pas commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # détecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        # détecter si le clic gauche de la souris est enfoncé
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.player.launch_projectile()
            # vérifier si la souris clic sur play
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



