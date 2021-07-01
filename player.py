import pygame
from projectile import Projectile


# class player

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/reda/player_final-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 510

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        if self.health > 100:
            x = (0, 102, 204)
            self.attack = 34
        elif self.health <= 100 and self.health > 60:
            x = (111, 210, 46)
            self.attack = 25
        elif self.health <= 60 and self.health > 40:
            x = (255, 255, 0)
            self.attack = 25
        elif self.health <= 40 and self.health > 20:
            x = (255, 128, 0)
        else:
            x = (255, 0, 0)
        pygame.draw.rect(surface, (255, 255, 255), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, x, [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play("tir")
