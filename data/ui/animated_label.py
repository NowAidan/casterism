import pygame

from data.core.settings import DEFAULT_FONT_PATH, DEFAULT_FONT_COLOUR, DEFAULT_TEXT_SPEED
from data.ui.label import Label

PUNCTUATION: list[str] = [".", ",", "!", "?"]

# times rewritten: 6 (worth it)

class AnimatedLabel(Label):
    def __init__(self, text: str, position: tuple, speed: int = DEFAULT_TEXT_SPEED, font_size: int = 20, colour: pygame.Color = DEFAULT_FONT_COLOUR, font: str = DEFAULT_FONT_PATH, do_anti_aliasing: bool = False) -> None:
        super().__init__(text, position, font_size, colour, font, do_anti_aliasing)
        
        self.surface: pygame.Surface = self.font.render("", do_anti_aliasing, colour)
        
        self.speed: int = speed
        self.punctuation_speed: int = 15
        
        self.character_index: int = 0
        
        self.punctuation_timer: int = 0
        self.typing_timer: int = 0
        
        self.is_typing: bool = True
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.character_index >= len(self.text): # stop the animation once the text has been fully typed.
            self.is_typing = False
        elif self.punctuation_timer > 0: # if punctuation was just shown, pause for some time before resuming.
            self.punctuation_timer += 1
            
            if self.punctuation_timer >= self.punctuation_speed:
                self.punctuation_timer = 0
        else: 
            self.typing_timer += 1
            
            if self.typing_timer >= self.speed:
                self.typing_timer = 0
                
                # sets the current character_index
                character: str = self.text[self.character_index]
                self.character_index += 1
                
                # if a character is a punctuation symbol, start the punctuation timer
                if character in PUNCTUATION:
                    self.punctuation_timer = 1
        
        # index of 0:self.counter splits the text from the start to the current character index (only rendering what has currently been typed)
        self.surface = self.font.render(self.text[0:self.character_index], self.do_anti_aliasing, self.colour)

        screen.blit(self.surface, (self.position[0], self.position[1] + self.y_offset))
    
    def skip_animation(self) -> None:
        self.is_typing = False
        self.character_index = len(self.text) # renders all of the text