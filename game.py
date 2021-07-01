import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from time import sleep
from sounds import SoundManager


# classe representant le jeu

class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # generer joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # gerer son
        self.sound_manager = SoundManager()
        # generer evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # mettre le compteur à 0
        self.font = pygame.font.Font("assets/Anton-Regular.ttf", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remmetre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('gameover')
        sleep(3)

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (255, 0, 0))
        screen.blit(score_text, (20, 20))
        # appliquer l'image de mon joueur

        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre d'event dl game
        self.comet_event.update_bar(screen)

        # recuperer projectiles

        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer monstres

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            self.player.update_health_bar(screen)

        # recuperer comet

        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer image projectile

        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre

        self.all_monsters.draw(screen)

        # appliquer image commet
        self.comet_event.all_comets.draw(screen)

        # gauche ou droite

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1050:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 10:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
