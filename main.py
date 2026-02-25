import pygame, sys
from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from support import *
from data import Data
from debug import debug
from ui import UI
from screens import MainMenu, SuccessScreen, GameOverScreen, CompleteScreen, PauseMenu, NameInputScreen, LeaderboardScreen
from os.path import join
import requests

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pyrates! Sail the high seas!")
        self.clock = pygame.time.Clock()
        self.import_assets()
        self.ui = UI(self.font, self.ui_frames)

        self.total_score = 0  # Accumulated score
        self.player_name = "Player"
        self.data_sent = False

        self.main_menu = MainMenu(self.display_surface, self.font)
        self.pause_menu = PauseMenu(self.display_surface, self.font)
        
        self.state = "name_input"

        self.tmx_maps = {
            0: load_pygame('./data/levels/tutorial.tmx'),
            1: load_pygame('./data/levels/1.tmx'),
            2: load_pygame('./data/levels/2.tmx'),
            3: load_pygame('./data/levels/3.tmx'),
            4: load_pygame('./data/levels/4.tmx'),
            5: load_pygame('./data/levels/5.tmx'),
        }
        self.current_level_index = 0

        self.current_stage = None
        self.data = None

        self.success_screen = None
        self.gameover_screen = None
        self.complete_screen = None

    def import_assets(self):
        # Import level assets using your support functions
        self.level_frames = {
            'flag': import_folder('graphics', 'level', 'flag'),
            'saw': import_folder('graphics', 'enemies', 'saw', 'animation'),
            'floor_spike': import_folder('graphics', 'enemies', 'floor_spikes'),
            'palms': import_sub_folders('graphics', 'level', 'palms'),
            'candle': import_folder('graphics', 'level', 'candle'),
            'window': import_folder('graphics', 'level', 'window'),
            'big_chain': import_folder('graphics', 'level', 'big_chains'),
            'small_chain': import_folder('graphics', 'level', 'small_chains'),
            'candle_light': import_folder('graphics', 'level', 'candle light'),
            'player': import_sub_folders('graphics', 'player'),
            'saw_chain': import_image('graphics', 'enemies', 'saw', 'saw_chain'),
            'helicopter': import_folder('graphics', 'level', 'helicopter'),
            'boat': import_folder('graphics', 'objects', 'boat'),
            'spike': import_image('graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
            'spike_chain': import_image('graphics', 'enemies', 'spike_ball', 'spiked_chain'),
            'tooth': import_folder('graphics', 'enemies', 'tooth', 'run'),
            'shell': import_sub_folders('graphics', 'enemies', 'shell'),
            'pearl': import_image('graphics', 'enemies', 'bullets', 'pearl'),
            'items': import_sub_folders('graphics', 'items'),
            'particle': import_folder('graphics', 'effects', 'particle'),
            'water_top': import_folder('graphics', 'level', 'water', 'top'),
            'water_body': import_image('graphics', 'level', 'water', 'body'),
            'bg_tiles': import_folder_dict('graphics', 'level', 'bg', 'tiles'),
            'cloud_small': import_folder('graphics', 'level', 'clouds', 'small'),
            'cloud_large': import_image('graphics', 'level', 'clouds', 'large_cloud'),
        }
        self.font = pygame.font.Font(join('graphics', 'ui', 'runescape_uf.ttf'), 40)
        self.ui_frames = {
            'heart': import_folder('graphics', 'ui', 'heart'),
            'coin': import_image('graphics', 'ui', 'coin'),
        }

    def start_game(self):
        self.data = Data(self.ui)
        self.current_stage = Level(self.tmx_maps[self.current_level_index], self.level_frames, self.data, self.current_level_index)
        self.state = "game"

    def next_level(self):
        self.total_score += self.data.coins
        self.current_level_index += 1
        # Check if there is a next level
        if self.current_level_index not in self.tmx_maps:
            # No more levels: go to game complete screen.
            self.state = "complete"
            # Use the final score from data
            score = self.total_score
            self.complete_screen = CompleteScreen(self.display_surface, self.font, score, self.player_name)
        else:
            self.start_game()

    def run(self):

        if self.state == "name_input":
            name_input_screen = NameInputScreen(self.display_surface, self.font)
            while name_input_screen.active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    name_input_screen.handle_event(event)
                name_input_screen.draw()
            self.player_name = name_input_screen.input_text.strip() or "Player"
            self.state = "menu"

        leaderboard_screen = None

        while True:
            dt = self.clock.tick() / 1000

            # New branch to handle name input state mid-game.
            if self.state == "name_input":
                name_input_screen = NameInputScreen(self.display_surface, self.font)
                while name_input_screen.active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        name_input_screen.handle_event(event)
                    name_input_screen.draw()
                self.player_name = name_input_screen.input_text.strip() or "Player"
                self.state = "menu"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "game":
                    if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_p):
                        self.state = "pause"
                        continue

                if self.state == "menu":
                    action = self.main_menu.handle_event(event)
                    if action == "start":
                        self.start_game()
                    elif action == "leaderboard":
                        leaderboard_screen = LeaderboardScreen(self.display_surface, self.font)
                        self.state = "leaderboard"
                elif self.state == "pause":
                    action = self.pause_menu.handle_event(event)
                    if action == "resume":
                        self.state = "game"
                    elif action == "quit":
                        self.state = "menu"
                elif self.state == "success":
                    action = self.success_screen.handle_event(event)
                    if action == "next":
                        self.next_level()
                elif self.state == "gameover":
                    action = self.gameover_screen.handle_event(event)
                    if action == "restart":
                        self.start_game()
                elif self.state == "complete":
                    # game_data = {
                    #     'name': self.player_name,
                    #     'score': self.total_score
                    # }
                    # url= "http://localhost/process_game.php"
                    # if not self.data_sent:
                    #     requests.post(url, game_data)
                    #     self.data_sent = True
                    # action = self.complete_screen.handle_event(event)
                    if action == "name_input":
                        self.state = "name_input"
                elif self.state == "leaderboard":
                    action = leaderboard_screen.handle_event(event)
                    if action == "menu":
                        self.state = "menu"

            if self.state == "menu":
                self.main_menu.draw()
            elif self.state == "game":
                self.current_stage.run(dt)
                self.ui.update(dt)
                if self.current_stage.finished:
                    score = self.data.coins
                    level_data = {
                        'level': self.current_level_index,
                        'user_name': self.player_name,
                        'score': score,
                    }
                    # url = "http://localhost/process_level.php"
                    # requests.post(url, level_data)
                    self.success_screen = SuccessScreen(self.display_surface, self.font, score)
                    self.data.coins = 0
                    self.state = "success"
                elif self.data.health <= 0:
                    score = self.data.coins
                    self.gameover_screen = GameOverScreen(self.display_surface, self.font, score)
                    self.state = "gameover"
            elif self.state == "pause":
                self.pause_menu.draw()
            elif self.state == "leaderboard":
                leaderboard_screen.draw()
            elif self.state == "success":
                self.success_screen.draw()
            elif self.state == "gameover":
                self.gameover_screen.draw()
            elif self.state == "complete":
                self.complete_screen.draw()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
