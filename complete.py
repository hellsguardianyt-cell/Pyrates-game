import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class CompleteScreen:
    def __init__(self, surface, font, score):
        self.display_surface = surface
        self.font = font
        self.score = score

        # Title text: Congratulations!
        self.title = self.font.render("Congratulations!", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        
        # Subtitle text: Game Completed & thanks message.
        self.subtitle = self.font.render("You've completed the game. Thanks for playing!", True, (255, 255, 255))
        self.subtitle_rect = self.subtitle.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        # Score text.
        self.score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * 2 // 3))
        
        # Optionally, add a button to go back to menu or exit.
        self.button_text_str = "Main Menu"
        self.text_color = (0, 0, 0)
        self.button_color = (100, 200, 100)
        padding_x, padding_y = 20, 10
        button_text_surface = self.font.render(self.button_text_str, True, self.text_color)
        self.button_rect = button_text_surface.get_rect()
        self.button_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 5 // 6)

    def draw(self):
        self.display_surface.fill("Black")
        self.display_surface.blit(self.title, self.title_rect)
        self.display_surface.blit(self.subtitle, self.subtitle_rect)
        self.display_surface.blit(self.score_text, self.score_rect)
        pygame.draw.rect(self.display_surface, self.button_color, self.button_rect, border_radius=10)
        button_text = self.font.render(self.button_text_str, True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.display_surface.blit(button_text, button_text_rect)

    def handle_event(self, event):
        # If the user clicks the button, return an action (e.g., "menu")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "menu"
        return None
