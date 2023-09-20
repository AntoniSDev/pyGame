import pygame

# classe de gestion du projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner l'image du projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # vérifier si le projectile entre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()

        # condition pour vérifier si le projectile sort de l'écran
        if self.rect.x > 1020:
            # supprimer le projectile
            self.remove()


