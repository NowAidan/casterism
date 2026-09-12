import pygame
import os

from data.ui.label import Label
from data.ui.animated_label import AnimatedLabel

FONT_PATH: str = os.path.join("assets", "fonts", "monogram.ttf")
FONT_SIZE: int = 40

MESSAGE_X_OFFSET: int = 16
MESSAGE_SPACING: int = 24


class MessageEntry:
    def __init__(self, message: list) -> None:
        self.text_labels: list[Label | AnimatedLabel] = []
        
        self.is_typing: bool = False

        self.y: int = 0
        self.y_offset: int = 0

        self.create_text(message)

    def draw(self, screen: pygame.Surface) -> None:
        for text_label in self.text_labels:
            text_label.y_offset = self.y_offset
            text_label.draw(screen)

            if isinstance(text_label, AnimatedLabel):
                if text_label.is_typing:
                    self.is_typing = True
                    
                    # draw runs every "tick"
                    # so, dont draw the next AnimatedLabel unless current one is finished typing/animating in
                    # this ensures only one AnimatedLabel is typing at a time
                    break
                
                self.is_typing = False

    def get_height(self) -> int:
        if self.text_labels:
            previous_label: Label | AnimatedLabel = self.text_labels[-1]
            
            return previous_label.position[1] - self.y + previous_label.height
        
        return MESSAGE_SPACING

    def set_y(self, y: int) -> None:
        old_y = self.y
        self.y = y

        # move all labels when the y is changed
        for text_label in self.text_labels:
            text_label.position = (text_label.position[0], y + text_label.position[1] - old_y)

    def create_text(self, message: list) -> None:
        message_current_x: int = MESSAGE_X_OFFSET
        message_current_y: int = self.y
        message_line_x: int = MESSAGE_X_OFFSET

        # create main message text
        for text_segment in message:
            # start a new line if the TextSegment has the new_line attribute set to True
            if text_segment.new_line and self.text_labels:
                message_current_x = message_line_x
                message_current_y += self.text_labels[-1].height
            
            text_label: AnimatedLabel = AnimatedLabel(
                text_segment.text,
                (message_current_x, message_current_y),
                text_segment.speed,
                FONT_SIZE,
                text_segment.colour,
                FONT_PATH,
            )           
            
            self.text_labels.append(text_label)
            
            # positions the new segment of text directly after the previous one
            message_current_x += text_label.width
    
    def skip_animation(self) -> None:
        for label in self.text_labels:
            if isinstance(label, AnimatedLabel):
                label.skip_animation()