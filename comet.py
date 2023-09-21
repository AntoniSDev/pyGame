import pygame


# créer la comet
class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # définir l'image de la comet
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
