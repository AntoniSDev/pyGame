import pygame
from player import Player
# créer la classe jeu
class Game:

    def __init__(self):
        # générer le player
        self.player = Player()
        self.pressed = {}

