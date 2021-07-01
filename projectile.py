import pygame


# definir la classe qui va gérer le projectile de notre joueur

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load('assets/R879c344569f0ee72ae58329b3e461924.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 70
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.image = pygame.transform.rotozoom(self.origin_image, 180, 1)
        self.angle = 130

    def rotate(self):
        self.angle -= 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # degats
            monster.damage(self.player.attack)

        if self.rect.x > 1100:
            self.remove()
