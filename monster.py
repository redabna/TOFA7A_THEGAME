import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.05
        self.image = pygame.image.load("assets/reda/ahalli-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image2 = pygame.image.load("assets/reda/ahalli2-removebg-preview-removebg-preview.png")
        self.image2 = pygame.transform.scale(self.image2, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(-100, 100)
        self.rect.y = 440
        self.velocity = random.randint(1, 2)

    def damage(self, amount):

        # infliger degats
        self.health -= amount

        # verifier si son nouveau nombre de point de vie est negatif

        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(-100, 100)
            self.health = self.max_health
            self.velocity = random.randint(1, 3 + self.game.score // 300)
            self.game.score += 5
            self.attack = 0.05 + self.game.score / 10000

    def update_health_bar(self, surface):
        if self.health <= 100 and self.health > 60:
            x = (111, 210, 46)
        elif self.health <= 60 and self.health > 40:
            x = (255, 255, 0)
        elif self.health <= 40 and self.health > 20:
            x = (255, 128, 0)
        else:
            x = (255, 0, 0)
        pygame.draw.rect(surface, (255, 255, 255), [self.rect.x + 50, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, x, [self.rect.x + 50, self.rect.y - 20, self.health, 5])
        self.image, self.image2 = self.image2, self.image

    def forward(self):
        # deplacement sans collisions
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        # si le monstre est en collision avec le joueur

        else:
            self.game.player.damage(self.attack)
