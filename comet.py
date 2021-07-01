import pygame
import random


# class gestion

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir image associé
        self.image = pygame.image.load('assets/reda/27156.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 900)
        self.velocity = random.randint(1, 2)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('tofa7a')

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 550:
            self.remove()

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")
            # retirer la boule
            self.remove()
            # zidlo dem :
            self.comet_event.game.player.health += 5
