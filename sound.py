import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("./assests/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("./assests/sounds/game_over.ogg"),
            "meteorite": pygame.mixer.Sound("./assests/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("./assests/sounds/tir.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
