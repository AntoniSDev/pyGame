import pygame
from comet import Comet

# créer une classe pour gérer l'evenement
class CometFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

        # définir un groupe de sprites comet
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += 1

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # apparaitre 1ere comete
        self.all_comets.add(Comet())

    def attempt_fall(self):
        # la jauge est full
        if self.is_full_loaded():
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):

        # ajouter du percent à la barre
        self.percent += self.percent_speed / 100

        # appel de la méthode attempt commet fall
        self.attempt_fall()

        # background de la barre
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            surface.get_width(),  # longeur de la fenêtre
            10  # epaisseur de la barre
        ])
        # barre d'event
        pygame.draw.rect(surface, (255, 120, 150), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longeur de la fenêtre
            10  # epaisseur de la barre
        ])
