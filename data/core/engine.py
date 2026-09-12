import pygame

import data.core.settings as settings
from data.core.game import Game

pygame.init()

class Engine:
    def __init__(self) -> None:
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        
        self.game_running: bool = True
        # pygame.SCALED preserves the intended resolution whilst also allowing for fullscreen
        self.screen: pygame.Surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.game: Game = Game()
    
    # update step for core engine logic
    def engine_update(self) -> None:
        while self.game_running:
            events: list[pygame.Event] = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.game_running = False
                
                # only call input() when a key is pressed
                if event.type == pygame.KEYDOWN:
                    keys: tuple = pygame.key.get_pressed()

                    self.input(keys)
                
            # this differs from input in that it reads from pygame's internal event queue
            # input on the other hand pulls from the hardware
            # the use of event is relatively niche but it still a necessary addition
            self.event(events)
            
            # calculates delta time
            delta: float = self.clock.tick(settings.FPS) / 1000
            
            self.update(delta)
            
            if self.game.scene_changed:
                # throw away the time spent constructing/loading the new scene
                # this fixes a MAJOR issue with fading in on a new scene not working due to the clock ticking whilst the scene is transitioning.
                self.clock.tick()
            
            self.draw(self.screen)
            
            pygame.display.flip()
            
        pygame.quit()
    
    # event step for pygame events
    def event(self, events: list[pygame.Event]) -> None:
        self.game.event(events)
        
    # input step for keyboard input
    def input(self, keys: tuple) -> None:
        self.game.input(keys)
        
    # update step for game logic
    def update(self, delta: float) -> None:
        self.game.update(delta)
    
    # draw step for game assets
    def draw(self, screen: pygame.Surface) -> None:
        self.game.draw(screen)