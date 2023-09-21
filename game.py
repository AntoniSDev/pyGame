import pygame
from player import Player
from monster import Monster


# créer la classe jeu
class Game:

    def __init__(self):
        # définir si notre jeu a commencé
        self.is_playing = False
        # générer le player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.monster_spawn_count = 0  # Compteur de monstres
        self.max_monsters = 2  # Nombre maximum de monstres à l'écran

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu au début
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du player
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du player
        self.player.update_health_bar(screen)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        # verifier la direction du joueur
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        if self.monster_spawn_count < self.max_monsters:
            monster = Monster(self)
            self.all_monsters.add(monster)
            self.monster_spawn_count += 1  # Incrémente le compteur de monstres
