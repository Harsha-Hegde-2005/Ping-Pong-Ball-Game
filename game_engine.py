import os
import random
import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Initialize mixer before sound use
        pygame.mixer.init()

        # Game objects
        self.player = Paddle(10, height // 2 - 50, 10, 100)
        self.ai = Paddle(width - 20, height // 2 - 50, 10, 100)
        self.ball = Ball(width // 2, height // 2, 7, WHITE, random.choice([-5, 5]), random.choice([-3, 3]))

        # Game state
        self.player_score = 0
        self.ai_score = 0
        self.winning_score = 5
        self.font = pygame.font.SysFont("Arial", 30)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        # Scoring logic
        if self.ball.x - self.ball.radius <= 0:
            self.ai_score += 1
            self.ball.score_sound.play()
            self.ball.reset_position(self.width, self.height)
        elif self.ball.x + self.ball.radius >= self.width:
            self.player_score += 1
            self.ball.score_sound.play()
            self.ball.reset_position(self.width, self.height)

        self.ai.auto_track(self.ball, self.height)
        self.check_game_over()

    def render(self, screen):
        screen.fill((0, 0, 0))

        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect)
        pygame.draw.rect(screen, WHITE, self.ai.rect)

        self.ball.draw(screen)

        # Center line
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

    def check_game_over(self):
        winner_text = ""
        if self.player_score >= self.winning_score:
            winner_text = "Player Wins!"
        elif self.ai_score >= self.winning_score:
            winner_text = "AI Wins!"

        if winner_text:
            self.winning_score = self.show_game_over_menu(winner_text)

    def show_game_over_menu(self, winner_text):
        font_title = pygame.font.SysFont("Arial", 60)
        font_option = pygame.font.SysFont("Arial", 40)
        options = ["Best of 3", "Best of 5", "Best of 7", "Exit"]
        running_menu = True
        winning_score = 5  # default

        screen = pygame.display.get_surface()

        while running_menu:
            screen.fill((0, 0, 0))

            # Render winner text
            text_surface = font_title.render(winner_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 4))
            screen.blit(text_surface, text_rect)

            # Render options
            for i, option in enumerate(options):
                option_surface = font_option.render(option, True, (200, 200, 200))
                option_rect = option_surface.get_rect(center=(self.width // 2, self.height // 2 + i * 60))
                screen.blit(option_surface, option_rect)

            pygame.display.flip()

            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        winning_score = 2  # Best of 3 → first to 2
                        running_menu = False
                    elif event.key == pygame.K_5:
                        winning_score = 3  # Best of 5 → first to 3
                        running_menu = False
                    elif event.key == pygame.K_7:
                        winning_score = 4  # Best of 7 → first to 4
                        running_menu = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

        # Reset scores and ball for replay
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset_position(self.width, self.height)
        return winning_score
