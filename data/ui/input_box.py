import pygame

from data.core.settings import DEFAULT_FONT_PATH, HELD_KEY_REPEAT_DELAY, HELD_KEY_REPEAT_INTERVAL
from data.ui.button import Button
from data.ui.label import Label

CURSOR_FLASH_TIME: int = 500 # in miliseconds
DEFAULT_BORDER_COLOUR: pygame.Color = pygame.Color(255, 255, 255)
TEXT_CURSOR_X_OFFSET: int = 5

class InputBox(Button):
    def __init__(self, text: str, position: tuple[int, int], box_width: int = 350, box_height: int = 0, text_alignment: str = "left", max_characters: int = 32, font_size: int = 30, colour: pygame.Color = pygame.Color(255, 255, 255), font: str = DEFAULT_FONT_PATH, do_anti_aliasing: bool = False) -> None:
        super().__init__(text, position, font_size, colour, font, do_anti_aliasing)
        
        self.submitted_text: str | None = None
        
        self.text_cursor: Label = Label("_", (0, 0), font_size) # underscore is used as a visual cursor indicator
        
        self.text_cursor_visible: bool = True
        
        self.max_characters: int = max_characters
        
        self.text_alignment: str = text_alignment
        
        self.box_width: int = box_width
        self.box_height: int = box_height
        
        self.cosmetic_rect: pygame.Rect = pygame.Rect(0, 0, box_width, box_width) # represents the visible box
        
        self.text_offset_x: int = 0
        self.text_offset_y: int = 0
        
        self.can_toggle: bool = True
        
        self.max_characters_reached: bool = False

        self.toggle_mode = True
        
        self.set_text(self.text)
        
        # allows keys to repeatly trigger if they are being held down
        pygame.key.set_repeat(HELD_KEY_REPEAT_DELAY, HELD_KEY_REPEAT_INTERVAL)
    
    def event(self, events: list[pygame.Event]) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # allows for the input box to always be active
                if not self.can_toggle:                  
                    return
                
                self.is_pressed()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.set_text(self.text[:-1])
                    return
                
                if event.key == pygame.K_RETURN:
                    if self.max_characters_reached:
                        return
                    
                    self.submitted_text = self.text.strip()
                    self.set_text("")
                    return
            
            # ignores keyboard input if the input box is not toggled
            if not self.is_toggled:
                return
            
            # check to see if the user has inputted text longer than the max_characters limit
            if len(self.text) > self.max_characters:
                self.max_characters_reached = True
            else:
                self.max_characters_reached = False
            
            # without running this check some text input will get missed every now and then
            if event.type == pygame.TEXTINPUT:
                self.set_text(self.text + event.text)
    
    def draw(self, screen: pygame.Surface) -> None:
        text_x: int = 0
        text_y: int = 0
        
        # calculates the horizontal position of the text depending on the specificied alignment.
        if self.text_alignment.lower() == "left":
            text_x = self.cosmetic_rect.left
        elif self.text_alignment.lower() == "center":
            text_x = self.cosmetic_rect.centerx - self.width // 2
        elif self.text_alignment.lower() == "right":
            text_x = self.cosmetic_rect.right - self.width
        
        text_x += self.text_offset_x
        text_y = self.cosmetic_rect.centery - self.height // 2 + self.text_offset_y
        
        self.rect.topleft = (text_x, text_y)
        
        screen.blit(self.surface, (text_x, text_y))
        
        # if the input box is selected
        if self.is_toggled:
            # change visibility every however many miliseconds assigned to CURSOR_FLASH_TIME
            self.text_cursor_visible = (pygame.time.get_ticks() // CURSOR_FLASH_TIME) % 2 == 0
            
            self.draw_text_cursor(screen, text_x, text_y)
    
    def draw_text_cursor(self, screen: pygame.Surface, text_x: int, text_y: int) -> None:
        if not self.text_cursor_visible:
            return
        
        # position the cursor directly after the typed text
        cursor_x = text_x + self.width + TEXT_CURSOR_X_OFFSET
        
        self.text_cursor.rect.topleft = (cursor_x, text_y)
        
        screen.blit(self.text_cursor.surface, self.text_cursor.rect)
    
    def set_text(self, text: str) -> None:
        super().set_text(text)
    
        self.cosmetic_rect.width = self.box_width
        
        # if box height is zero, scale height to text height with some padding
        if self.box_height == 0:
            self.cosmetic_rect.height = self.height
        else:
            self.cosmetic_rect.height = self.box_height
        
        self.cosmetic_rect.topleft = self.position
        
        self.rect = self.surface.get_rect(topleft = self.position)
        
        self.collision_rect = self.cosmetic_rect.copy()
    
    def get_submitted_text(self) -> str | None:
        if self.submitted_text:
            text: str = self.submitted_text
            self.submitted_text = None
            
            return text