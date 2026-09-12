import pygame

from data.core.settings import DEFAULT_FONT_PATH, DEFAULT_FONT_COLOUR

class Label:
    def __init__(self, text: str, position: tuple[int, int], font_size: int = 20, colour: pygame.Color = DEFAULT_FONT_COLOUR, font: str = DEFAULT_FONT_PATH, do_anti_aliasing: bool = False) -> None:
        self.text: str = text
        self.position: tuple[int, int] = position
        self.colour: pygame.Color = colour
        
        self.do_anti_aliasing: bool = do_anti_aliasing
        self.use_rect_positioning: bool = False
        
        self.font: pygame.font.Font = pygame.font.Font(font, font_size)
        
        self.surface: pygame.Surface = self.render()
        self.rect: pygame.Rect = self.surface.get_rect(topleft = self.position)
        
        self.width: int = self.surface.get_width()
        self.height: int = self.surface.get_height()
        
        self.y_offset: int = 0
        
    def render(self) -> pygame.Surface:
        return self.font.render(self.text, self.do_anti_aliasing, self.colour)
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.use_rect_positioning: # blitting with a rect allows more precise positioning anchored around screen areas
            screen.blit(self.surface, self.rect)
        else:
            screen.blit(self.surface, (self.position[0], self.position[1] + self.y_offset))
    
    def set_text(self, text: str) -> None:
        self.text = text
        
        # re-render the surface as the text has been changed
        self.surface = self.render()
        
        # update the rect and dimensions because changing the text can change the size of the rendered surface
        self.rect = self.surface.get_rect(topleft = self.position)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()