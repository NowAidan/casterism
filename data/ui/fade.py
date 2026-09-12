import pygame

from data.core.settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Fade():
    def __init__(self, speed: int = 255, colour: pygame.Color = pygame.Color(0, 0, 0)) -> None:
        self.speed: int = speed
        self.surface: pygame.Surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.colour: pygame.Color = colour
        self.alpha: int = 0
        self.fade_direction: int = 0 # 1 for fading in, 0 for not fading, -1 for fading out
        self.is_finished: bool = True
        
        self.surface.fill(self.colour)
    
    def fade_in(self) -> None:
        # start fully opaque
        self.alpha = 255
        self.fade_direction = -1
        self.is_finished = False
        self.surface.set_alpha(self.alpha)
    
    # and vice versa
    def fade_out(self) -> None:
        # start fully transparent
        self.alpha = 0
        self.fade_direction = 1
        self.is_finished = False
        self.surface.set_alpha(self.alpha)
    
    def update(self, delta: float) -> None:
        if self.is_finished:
            return
        
        # +- turns to - which means it accounts for fade_direction
        self.alpha += int(self.fade_direction * self.speed * delta)
        
        # clamp the surface's alpha value and finishing fading
        if self.alpha >= 255:
            self.alpha = 255
            self.is_finished = True
        elif self.alpha <= 0:
            self.alpha = 0
            self.is_finished = True
            
        self.surface.set_alpha(self.alpha)

    def draw(self, screen: pygame.Surface) -> None:
        if self.alpha > 0:
            screen.blit(self.surface, (0, 0))
    
    def set_speed(self, speed: int) -> None:
        # prevents an invalid speed
        if speed <= 0:
            return
        
        self.speed = speed