import pygame
import random


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
        # here
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.rand_xd = random.choice([-1, 1])
        self.rand_yd = random.choice([-1, 1])

    def update(self, screen_rect):
        self.rect = self.rect.move(
            self.rand_xd*self.speed, self.rand_yd*self.speed)

        self.screen_rect = screen_rect
        if self.rect.left < screen_rect.left + 200 or self.rect.right > screen_rect.right - 200:
            self.rand_xd = -self.rand_xd
        elif self.rect.top < screen_rect.top or self.rect.bottom > screen_rect.bottom:
            self.rand_yd = -self.rand_yd
