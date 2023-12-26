import pygame
import random
import animation


class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset

        self.start_animation()

    def set_speed(self, speed):
        self.defautl_speed = speed
        self.velocity = random.randint(50, 100) / 100

    def damage(self, amount):
        # infliger degat
        self.health -= amount
        if self.health <= 0:
            # reaparaitre comme nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.health_max
            self.velocity = self.defautl_speed
            self.game.add_score(20)

            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)
            self.game.comet_event.attempt_fall()

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def bar(self, surface):
        # definir une coulour jauge devie vert clair

        # position largeur epaissair bar de vie

        # dessiner la bar
        pygame.draw.rect(
            surface,
            (60, 63, 60),
            [self.rect.x + 10, self.rect.y - 20, self.health_max, 5],
        )
        pygame.draw.rect(
            surface,
            (111, 210, 46),
            [self.rect.x + 10, self.rect.y - 20, self.health, 5],
        )

    def update_animation(self):
        self.animate(loop=True)

    def forward(self):
        if not self.game.check_colision(self, self.game.all_player):
            self.rect.x -= self.velocity

        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.health_max = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)
