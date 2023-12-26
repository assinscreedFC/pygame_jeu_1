import pygame
from projectile import Projectile
import animation


# creer notre classe player
class Player(animation.AnimateSprite):
    def __init__(self, game):
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attacke = 10
        self.velocity = 3
        self.all_projectil = pygame.sprite.Group()
        # on appelle le constructeur de la class parente (Sprite) pour initialiser les attributs necessaires
        super().__init__("player")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def updte_animation(self):
        self.animate()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def bar(self, surface):
        pygame.draw.rect(
            surface,
            (60, 63, 60),
            [self.rect.x + 50, self.rect.y + 20, self.health_max, 5],
        )
        pygame.draw.rect(
            surface,
            (111, 210, 46),
            [self.rect.x + 50, self.rect.y + 20, self.health, 5],
        )

    def move_right(self):
        """Permet au joueur de se déplacer vers la droite"""
        if not self.game.check_colision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launche_projectil(self):
        # creer une nouvelle instance
        self.all_projectil.add(Projectile(self))
        self.game.sound_manager.play("tir")
        self.start_animation()
