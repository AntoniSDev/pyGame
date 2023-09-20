import pygame
import random

# créer une classe qui va gérer la notion de monstres
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        # infliger les dégats
        self.health -= amount

        # vérifier si ses pv sont à <=0
        if self.health <= 0:
            # réaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (110, 210, 45), [self.rect.x +10, self.rect.y -20, self.health, 5])

    def forward(self):
        # le déplacement ne se fait que si il n'y a pas de collision avec le groupe joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)