import pygame
import os

from data.ui.label import Label

DEFAULT_FONT: str = os.path.join("assets", "fonts", "Not Jam Mono Clean 16.ttf")
COLLISION_MARGIN_MULTIPLIER: float = 1.1

class Button(Label):
    def __init__(self, text: str, position: tuple[int, int], font_size: int = 30, colour: pygame.Color = pygame.Color(255, 255, 255), font: str = DEFAULT_FONT, do_anti_aliasing: bool = False) -> None:
        super().__init__(text, position, font_size, colour, font, do_anti_aliasing)
        
        self.collision_rect: pygame.Rect = pygame.Rect(self.position[0], self.position[1], self.width * COLLISION_MARGIN_MULTIPLIER, self.height * COLLISION_MARGIN_MULTIPLIER)
        self.toggle_mode: bool = False
        self.is_toggled: bool = False
        
    def render(self) -> pygame.Surface:
        surface: pygame.Surface = self.font.render(self.text, self.do_anti_aliasing, self.colour)
        
        return surface
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.use_rect_positioning:
            screen.blit(self.surface, self.rect)
        else:
            screen.blit(self.surface, self.position)
    
    def is_hovered(self) -> bool:
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        # is the mouse hovering over the collsion_rect for the button
        if self.collision_rect.collidepoint(mouse_pos):
            return True
        
        return False

    def is_pressed(self) -> bool:
        # tuple[is left click, is middle click, is right click]
        clicks: tuple[bool, bool, bool] = pygame.mouse.get_pressed()
        
        if self.is_hovered():
            if self.toggle_mode: # if the button is a toggle button, toggle on/off
                self.is_toggled = not self.is_toggled

                return self.is_toggled
            
            if clicks[0]: # if left clicked
                return True

        return False