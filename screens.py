import pygame
import requests
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class NameInputScreen:
    def __init__(self, surface, font):
        self.display_surface = surface
        self.font = font
        self.input_text = ""
        self.prompt = self.font.render("Enter your name:", True, (255, 255, 255))
        self.prompt_rect = self.prompt.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        self.input_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 25, 300, 50)
        self.active = True

    def draw(self):
        self.display_surface.fill("Black")
        self.display_surface.blit(self.prompt, self.prompt_rect)
        # Draw the input box
        pygame.draw.rect(self.display_surface, (255,255,255), self.input_rect, 2)
        # Render the current text.
        input_surface = self.font.render(self.input_text, True, (255, 255, 255))
        self.display_surface.blit(input_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False  # Finished input
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

class CompleteScreen:
    def __init__(self, surface, font, score, player_name):
        self.display_surface = surface
        self.font = font
        self.score = score
        self.player_name = player_name

        # Title text: Congratulations!
        self.title = self.font.render(f"Congratulations {self.player_name}!", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))

        # Personalized message.
        self.name_text = self.font.render("You've completed the game!", True, (255, 255, 255))
        self.name_rect = self.name_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2.5))
        
        # Score text.
        self.score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * 2 // 3))
        
        # Main Menu button.
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
        self.display_surface.blit(self.name_text, self.name_rect)
        self.display_surface.blit(self.score_text, self.score_rect)
        pygame.draw.rect(self.display_surface, self.button_color, self.button_rect, border_radius=10)
        button_text = self.font.render(self.button_text_str, True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.display_surface.blit(button_text, button_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "name_input"
        return None
    
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

class SuccessScreen:
    def __init__(self, surface, font, score):
        self.display_surface = surface
        self.font = font
        self.score = score

        self.title = self.font.render("Level Complete!", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        
        self.score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        self.button_text_str = "Next Level"
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
                return "next"
        return None

class MainMenu:
    def __init__(self, surface, font):
        self.display_surface = surface
        self.font = font
        
        self.menu_image = pygame.image.load('./graphics/menu/menu.jpg')
        self.menu_image = pygame.transform.scale(self.menu_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.start_text = "Start Game"
        self.leaderboard_text = "Leaderboard"
        self.text_color = (0, 0, 0)
        self.button_color = (100, 200, 100)
        
        # Create Start Game button.
        start_surf = self.font.render(self.start_text, True, self.text_color)
        padding_x, padding_y = 20, 10
        self.start_rect = start_surf.get_rect()
        self.start_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.start_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        
        # Create Leaderboard button.
        leaderboard_surf = self.font.render(self.leaderboard_text, True, self.text_color)
        self.leaderboard_rect = leaderboard_surf.get_rect()
        self.leaderboard_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.leaderboard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
        
        # Title
        self.title = self.font.render("Pyrates! Sail the High Seas!", True, (0, 0, 0))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        
    def draw(self):
        # Draw the menu background image
        self.display_surface.blit(self.menu_image, (0, 0))
        
        # Create a simple background for the title text
        title_bg_color = (255, 215, 0)  # Dark grey background color
        title_bg_padding = 20          # Increase or decrease for more/less padding
        title_bg_rect = self.title_rect.inflate(title_bg_padding, title_bg_padding)
        
        # Optionally, you can add a semi-transparent background by using a Surface with an alpha channel:
        title_bg_surface = pygame.Surface((title_bg_rect.width, title_bg_rect.height))
        title_bg_surface.set_alpha(180)  # Adjust transparency (0-255)
        title_bg_surface.fill(title_bg_color)
        self.display_surface.blit(title_bg_surface, title_bg_rect.topleft)
        
        # Draw the title text on top of the background
        self.display_surface.blit(self.title, self.title_rect)
        
        # Draw start button.
        pygame.draw.rect(self.display_surface, self.button_color, self.start_rect, border_radius=10)
        start_text = self.font.render(self.start_text, True, self.text_color)
        start_text_rect = start_text.get_rect(center=self.start_rect.center)
        self.display_surface.blit(start_text, start_text_rect)
        
        # Draw leaderboard button.
        pygame.draw.rect(self.display_surface, self.button_color, self.leaderboard_rect, border_radius=10)
        leaderboard_text = self.font.render(self.leaderboard_text, True, self.text_color)
        leaderboard_text_rect = leaderboard_text.get_rect(center=self.leaderboard_rect.center)
        self.display_surface.blit(leaderboard_text, leaderboard_text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_rect.collidepoint(event.pos):
                return "start"
            elif self.leaderboard_rect.collidepoint(event.pos):
                return "leaderboard"
        return None

class LeaderboardScreen:
    def __init__(self, surface, font):
        self.display_surface = surface
        self.font = font
        self.leaderboard_data = []  # list of dicts: e.g. [{'name': 'Player1', 'score': 100}, ...]
        self.fetch_data()
        
        self.title = self.font.render("Leaderboard", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH // 2, 50))
        
        # Create a back button.
        self.back_text = "Back to Menu"
        self.back_text_color = (0, 0, 0)
        self.back_button_color = (100, 200, 100)
        padding_x, padding_y = 20, 10
        back_surf = self.font.render(self.back_text, True, self.back_text_color)
        self.back_rect = back_surf.get_rect()
        self.back_rect.inflate_ip(padding_x * 2, padding_y * 2)
        self.back_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)

    def fetch_data(self):
        try:
            # Fetch overall leaderboard
            overall_response = requests.get("http://localhost/get_leaderboard.php")
            if overall_response.status_code == 200:
                self.leaderboard_data = overall_response.json()
            else:
                self.leaderboard_data = []
            
            # Fetch level-specific leaderboard
            level_response = requests.get("http://localhost/get_level_leaderboard.php")
            if level_response.status_code == 200:
                self.level_leaderboard_data = level_response.json()
            else:
                self.level_leaderboard_data = []
        except Exception as e:
            print("Error fetching leaderboard data:", e)
            self.leaderboard_data = []
            self.level_leaderboard_data = []

    def draw(self):
        self.display_surface.fill("Black")
        self.display_surface.blit(self.title, self.title_rect)
        
        # Define positions for the two columns.
        left_center_x = WINDOW_WIDTH // 4           # Left column center x-coordinate.
        right_center_x = 3 * WINDOW_WIDTH // 4        # Right column center x-coordinate.
        heading_y = 100                               # Starting y position for headings.
        
        # Draw overall leaderboard heading in left column.
        overall_heading = self.font.render("Overall Leaderboard", True, (255, 255, 255))
        overall_heading_rect = overall_heading.get_rect(center=(left_center_x, heading_y))
        self.display_surface.blit(overall_heading, overall_heading_rect)
        
        # Draw level high scores heading in right column.
        level_heading = self.font.render("Level High Scores", True, (255, 255, 255))
        level_heading_rect = level_heading.get_rect(center=(right_center_x, heading_y))
        self.display_surface.blit(level_heading, level_heading_rect)
        
        # Set initial y offsets for the entries (below the headings).
        left_y_offset = heading_y + 40
        right_y_offset = heading_y + 40
        
        # Display up to 10 overall leaderboard entries in the left column.
        for i, entry in enumerate(self.leaderboard_data[:10]):
            text = f"{i+1}. {entry['name']} - {entry['score']}"
            entry_surf = self.font.render(text, True, (255, 255, 255))
            entry_rect = entry_surf.get_rect(center=(left_center_x, left_y_offset))
            self.display_surface.blit(entry_surf, entry_rect)
            left_y_offset += 30  # Spacing between entries.
        
        # Process level_leaderboard_data to keep only one (best) entry per level.
        best_scores = {}
        for entry in self.level_leaderboard_data:
            level = entry['level']
            if level not in best_scores or entry['score'] > best_scores[level]['score']:
                best_scores[level] = entry
        # Sort by level number
        best_scores_list = [best_scores[level] for level in sorted(best_scores.keys())]
        
        # Display up to 10 entries from the processed list in the right column.
        for i, entry in enumerate(best_scores_list[:10]):
            text = f"Level {entry['level']}: {entry['user_name']} - {entry['score']}"
            entry_surf = self.font.render(text, True, (255, 255, 255))
            entry_rect = entry_surf.get_rect(center=(right_center_x, right_y_offset))
            self.display_surface.blit(entry_surf, entry_rect)
            right_y_offset += 30  # Spacing between entries.
        
        # Draw back button.
        pygame.draw.rect(self.display_surface, self.back_button_color, self.back_rect, border_radius=10)
        back_surf = self.font.render(self.back_text, True, self.back_text_color)
        back_rect_text = back_surf.get_rect(center=self.back_rect.center)
        self.display_surface.blit(back_surf, back_rect_text)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_rect.collidepoint(event.pos):
                return "menu"
        return None