import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class MainMenu:
    def __init__(self, surface, font):
        self.display_surface = surface
        self.font = font
        
        self.menu = pygame.image.load('./graphics/menu/menu.jpg')
        self.menu = pygame.transform.scale(self.menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.button_text_str = "Start Game"
        self.text_color = (0, 0, 0)  
        self.button_color = (100, 200, 100)  
        
        button_text_surface = self.font.render(self.button_text_str, True, self.text_color)
        padding_x, padding_y = 20, 10

        self.button_rect = button_text_surface.get_rect()
        self.button_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        self.title = self.font.render("Pyrates! Sail the High Seas!", True, (0, 0, 0))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))

    def draw(self):
        self.display_surface.blit(self.menu, (0, 0))
        
        self.display_surface.blit(self.title, self.title_rect)
        
        pygame.draw.rect(self.display_surface, self.button_color, self.button_rect, border_radius=10)
        
        button_text = self.font.render(self.button_text_str, True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.display_surface.blit(button_text, button_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "start"
        return None
