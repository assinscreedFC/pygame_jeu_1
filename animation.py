import pygame
import random


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load("./assests/" + name + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
            if loop is False:
                self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

    def load_animation_images(name):
        images = []
        path = f"./assests/{name}/{name}"
        for num in range(1, 24):
            img = pygame.image.load(path + str(num) + ".png")
            images.append(img)
        return images


animations = {
    "mummy": AnimateSprite.load_animation_images("mummy"),
    "player": AnimateSprite.load_animation_images("player"),
    "alien": AnimateSprite.load_animation_images("alien"),
}
