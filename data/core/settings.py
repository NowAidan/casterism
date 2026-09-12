import pygame
import os

WINDOW_CAPTION: str = "Catasterism"
WINDOW_WIDTH: int = 1280
WINDOW_HEIGHT: int = 720
WINDOW_WIDTH_CENTER: int = WINDOW_WIDTH // 2
WINDOW_HEIGHT_CENTER: int = WINDOW_HEIGHT // 2
FPS: float = 60

DEFAULT_SCENE: str = "main_menu"
DEFAULT_FONT_PATH: str = os.path.join("assets", "fonts", "monogram.ttf")
DEFAULT_FONT_COLOUR: pygame.Color = pygame.Color(255, 255, 255)
DEFAULT_TEXT_SPEED: int = 2
DEFAULT_LINE_SPEED: int = 2 # speed to wait before new lines.

HELD_KEY_REPEAT_DELAY: int = 350
HELD_KEY_REPEAT_INTERVAL: int = 50