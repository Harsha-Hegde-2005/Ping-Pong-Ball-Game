import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.speed = 7

        # Use a rect attribute for easy collision/drawing
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, dy, screen_height):
        self.rect.y += dy
        # Clamp inside screen
        self.rect.y = max(0, min(self.rect.y, screen_height - self.height))

    def auto_track(self, ball, screen_height):
        if ball.y < self.rect.top:
            self.move(-self.speed, screen_height)
        elif ball.y > self.rect.bottom:
            self.move(self.speed, screen_height)
