import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class PauseMenu:
    def __init__(self, surface, font):
        self.display_surface = surface
        self.font = font

        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.overlay.set_alpha(150)  
        self.overlay.fill((0, 0, 0))   

        
        self.title_text = self.font.render("Paused", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))

        padding_x, padding_y = 20, 10


        self.resume_button_text = "Resume"
        self.resume_text_color = (0, 0, 0)
        self.resume_button_color = (100, 200, 100)
        resume_text_surf = self.font.render(self.resume_button_text, True, self.resume_text_color)
        self.resume_button_rect = resume_text_surf.get_rect()
        self.resume_button_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.resume_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        self.quit_button_text = "Quit to Menu"
        self.quit_text_color = (0, 0, 0)
        self.quit_button_color = (200, 100, 100)
        quit_text_surf = self.font.render(self.quit_button_text, True, self.quit_text_color)
        self.quit_button_rect = quit_text_surf.get_rect()
        self.quit_button_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.quit_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 2 // 3)

    def draw(self):
        self.display_surface.blit(self.overlay, (0, 0))
        
        self.display_surface.blit(self.title_text, self.title_rect)
        
        pygame.draw.rect(self.display_surface, self.resume_button_color, self.resume_button_rect, border_radius=10)
        resume_text = self.font.render(self.resume_button_text, True, self.resume_text_color)
        resume_text_rect = resume_text.get_rect(center=self.resume_button_rect.center)
        self.display_surface.blit(resume_text, resume_text_rect)
        
        
        pygame.draw.rect(self.display_surface, self.quit_button_color, self.quit_button_rect, border_radius=10)
        
        quit_text = self.font.render(self.quit_button_text, True, self.quit_text_color)
        quit_text_rect = quit_text.get_rect(center=self.quit_button_rect.center)
        self.display_surface.blit(quit_text, quit_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                return "resume"
            elif self.quit_button_rect.collidepoint(event.pos):
                return "quit"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                return "resume"
        return None
