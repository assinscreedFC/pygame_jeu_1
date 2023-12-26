import pygame
from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent
from comet import Comet
from sound import SoundManager


class Game:
    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.comet_event = CometFallEvent(self)
        self.font = pygame.font.SysFont("monospace", 16)
        self.score = 0
        self.sound_manager = SoundManager()
        self.all_player.add(self.player)
        self.pressed = {}
        self.all_monster = pygame.sprite.Group()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, point=10):
        self.score += point

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.health_max
        self.is_playing = False
        self.sound_manager.play("game_over")

        self.score = 0

    def update(self, screen):
        score_text = self.font.render(f"score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectil:
            projectile.move()

        for monster in self.all_monster:
            monster.forward()
            monster.bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectil.draw(screen)
        self.comet_event.all_comets.draw(screen)
        self.player.bar(screen)
        self.comet_event.update_bar(screen)
        self.player.updte_animation()
        # appliquer les sprite de monstre
        self.all_monster.draw(screen)

        if (
            self.pressed.get(pygame.K_RIGHT)
            and self.player.rect.x + self.player.rect.width < screen.get_width()
        ):
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )

    def spawn_monster(self, monster_name):
        monster = Mummy(self)
        self.all_monster.add(monster_name.__call__(self))
