import pygame
import math
from game import Game

pygame.init()
# definir une clock
clock = pygame.time.Clock()
FPS = 30


pygame.display.set_caption("comet fall game")
pygame.display.set_mode((1080, 720))
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("./assests/bg.jpg")
banner = pygame.image.load("./assests/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
play_button = pygame.image.load("./assests/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
running = True
game = Game()

# boucle du jeu
while running:
    # appliquer l'arrier plan de notre jeu
    screen.blit(background, (0, -200))

    # si le jeux a commencer
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # condition de sortie
    for event in pygame.event.get():
        # event fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un player lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launche_projectil()
                else:
                    game.is_playing = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play("click")
    # fixer le nbr de fps
    clock.tick(FPS)
