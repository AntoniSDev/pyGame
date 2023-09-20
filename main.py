import pygame
from game import Game
pygame.init()

# générer la fenêtre du jeu
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

running = True

# boucle while running true
while running:

    # appliquer arrière plan du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image du player
    screen.blit(game.player.image, game.player.rect)

    # verifier la direction du joueur
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False