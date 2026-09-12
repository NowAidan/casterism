import pygame

#from player import Player
from data.scenes.scene import Scene
from data.scenes.main_menu import MainMenuScene

class Game():
    def __init__(self) -> None:
        self.current_scene: Scene = MainMenuScene()
        self.scene_changed: bool = False
    
    def event(self, events: list[pygame.Event]) -> None:
        self.current_scene.event(events)
        
    def input(self, keys: tuple) -> None:
        self.current_scene.input(keys)
    
    def update(self, delta: float) -> None:
        self.scene_changed = False
        
        self.current_scene.update(delta)
        
        # change the scene is a new scene is assigned to the current_scene's next_scene attribute
        if self.current_scene != self.current_scene.next_scene:
            self.current_scene = self.current_scene.next_scene
            self.scene_changed = True
    
    def draw(self, screen: pygame.Surface) -> None:
        self.current_scene.draw(screen)