import pygame

from typing import Self

class Scene:
    def __init__(self) -> None:
        self.next_scene: Scene = self
        self.attempting_scene_change: bool = False
    
    def event(self, events: list[pygame.Event]) -> None:
        pass # pass does nothing
    
    def input(self, keys: tuple) -> None:
        pass
    
    def update(self, delta: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass
    
    def change_scene(self, scene: Self) -> None:
        self.next_scene = scene