import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class GameOverScreen:
    def __init__(self, surface, font, score):
        self.display_surface = surface
        self.font = font
        self.score = score

        self.title = self.font.render("Game Over", True, (255, 0, 0))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        
        self.score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        self.button_text_str = "Restart Level"
        self.text_color = (0, 0, 0)
        self.button_color = (100, 200, 100)
        padding_x, padding_y = 20, 10
        
        button_text_surface = self.font.render(self.button_text_str, True, self.text_color)
        self.button_rect = button_text_surface.get_rect()
        self.button_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 2 // 3)

    def draw(self):
        self.display_surface.fill((0, 0, 0))
        self.display_surface.blit(self.title, self.title_rect)
        self.display_surface.blit(self.score_text, self.score_rect)
        pygame.draw.rect(self.display_surface, self.button_color, self.button_rect, border_radius=10)
        button_text = self.font.render(self.button_text_str, True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.display_surface.blit(button_text, button_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "restart"
        return None
