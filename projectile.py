import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load("./assests/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectil.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_colision(
            self, self.player.game.all_monster
        ):
            self.remove()
            # infliger degats
            monster.damage(self.player.attacke)

        if self.rect.x > 1080:
            self.remove()
