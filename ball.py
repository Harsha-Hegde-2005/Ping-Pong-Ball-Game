import pygame
import random

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = pygame.Rect(self.x - radius, self.y - radius, radius * 2, radius * 2)

        # Load sound effects (ensure mixer is initialized in main)
        self.paddle_sound = pygame.mixer.Sound("assets/paddle_hit.mp3")
        self.wall_sound = pygame.mixer.Sound("assets/wall_bounce.mp3")
        self.score_sound = pygame.mixer.Sound("assets/score.wav")

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

    def check_collision(self, player, ai):
        # Wall collision (top/bottom)
        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.speed_y *= -1
            self.wall_sound.play()

        # Paddle collisions
        if self.rect.colliderect(player.rect):
            self.speed_x = abs(self.speed_x)
            self.paddle_sound.play()

        if self.rect.colliderect(ai.rect):
            self.speed_x = -abs(self.speed_x)
            self.paddle_sound.play()

    def reset_position(self, screen_width, screen_height):
        """Reset ball to center and change direction randomly."""
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])
        self.score_sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
