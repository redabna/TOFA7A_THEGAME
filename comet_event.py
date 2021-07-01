import pygame
from comet import Comet


# creer classe pour gerer cet evenement

class CometFallEvent:

    # lores du chargement -> créer un compteur

    def __init__(self, game):
        self.percent = 0
        self.percentspeed = 10
        self.game = game
        # groupe de sprite
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percentspeed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # apparaitre lwla
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenement est totalement chargée
        if self.is_full_loaded():
            self.meteor_fall()
            self.percent = 0

    def update_bar(self, surface):
        self.add_percent()

        self.attempt_fall()
