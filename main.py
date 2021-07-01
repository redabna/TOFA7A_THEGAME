import pygame
from game import Game

pygame.init()

# génerer fenetre de jeu
pygame.display.set_caption("TOFA7A v1.0")
screen = pygame.display.set_mode((1215, 630))
gameIcon = pygame.image.load('assets/reda/27156.png')
pygame.display.set_icon(gameIcon)

# importer l'arrière plan de notre jeu

background = pygame.image.load('assets/reda/Raf47ad974f7d76277b2a61551b3e6444.jfif')
background = pygame.transform.scale(background, (1200, 700))

# importer bannière
banner = pygame.image.load('assets/TOFA7A1.png')
banner = pygame.transform.scale(banner, (500, 500))

# inmporter botona

botona = pygame.image.load('assets/pixlr-bg-result (1).png')
botona = pygame.transform.scale(botona, (400, 300))
botona_rect = botona.get_rect()
botona_rect.x = 400
botona_rect.y = 470

# charger jeu

game = Game()

running = True

# boucle tant que running vrai

while running:
    # appliquer l'arrière plan

    screen.blit(background, (8, -65))

    # verifier if game bda
    if game.is_playing:
        # bda la partie
        game.update(screen)

    # verifier si le jeu mabdach
    else:
        # ecran mr7ba
        screen.blit(banner, (370, 70))
        # botona
        screen.blit(botona, (415, 380))

    # mettre à jour l'écran

    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # si femeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        # si un joueur touche le clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    if len(game.player.all_projectiles)<=5:
                        game.player.launch_projectile()
                else:
                    game.start()
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if botona_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                game.sound_manager.play('click')
