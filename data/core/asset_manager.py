from typing_extensions import Self

import pygame

class AssetManager():
    def load_image(self, key: str, path: str) -> pygame.Surface:
        return pygame.image.load(path).convert_alpha()
    
    def load_sound(self, key: str, path: str) -> pygame.mixer.Sound:
        return pygame.mixer.Sound(path)