import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'gameover': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'tofa7a': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg")
        }

    def play(self,name):
        self.sounds[name].play()