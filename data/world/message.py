import pygame

from data.core.settings import DEFAULT_TEXT_SPEED

DEFAULT_MESSAGE_COLOUR: pygame.Color = pygame.Color(255, 255, 255)

class TextSegment:
    def __init__(self, text: str, colour: pygame.Color = DEFAULT_MESSAGE_COLOUR, speed: int = DEFAULT_TEXT_SPEED, new_line: bool = False):
        self.text: str = text
        self.colour: pygame.Color = colour
        self.speed: int = speed
        
        self.new_line: bool = new_line