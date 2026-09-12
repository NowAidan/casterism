import pygame
import os

from data.ui.label import Label
from data.ui.button import DEFAULT_FONT, Button
from data.utils.math_utils import lerp

HOVER_ICON_FONT_PATH: str = os.path.join("assets", "fonts", "Not Jam Mono Clean 16.ttf")

LERP_SPEED: float = 0.3

HOVER_OFFSET_X: float = 35.0
HOVER_OFFSET_Y: float = 0.0

class AnimatedButton(Button):
    def __init__(self, text: str, position: tuple[int, int], font_size: int = 30, colour: pygame.Color = pygame.Color(255, 255, 255), font: str = HOVER_ICON_FONT_PATH, do_anti_aliasing: bool = False) -> None:
        super().__init__(text, position, font_size, colour, font, do_anti_aliasing)
        
        self.hover_icon: Label = Label("→", (self.position), font_size, font=HOVER_ICON_FONT_PATH)
        self.default_position: tuple[int, int] = position
        self.offset_position: tuple[int, int] = (int(self.default_position[0] + HOVER_OFFSET_X), int(self.default_position[1] + HOVER_OFFSET_Y))
    
    def render(self) -> pygame.Surface:
        surface: pygame.Surface = self.font.render(self.text, self.do_anti_aliasing, self.colour)
        
        return surface

    def draw(self, screen: pygame.Surface) -> None:
       
        if self.is_hovered():
            self.hover_icon.draw(screen)
            
            # if hovered lerp the position of the button inwards, creating a hover effect
            self.position = (int(lerp(self.position[0], self.offset_position[0], LERP_SPEED)), self.offset_position[1])
        else:
            # if not hovered, lerp back to the normal position, animating back from the hover position if recently hovered
            self.position = (int(lerp(self.position[0], self.default_position[0], LERP_SPEED)), self.default_position[1])
        
        screen.blit(self.surface, self.position)