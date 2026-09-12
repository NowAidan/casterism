import pygame
import os
import sys

from data.core.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from data.core.asset_manager import AssetManager
from data.scenes.scene import Scene
from data.ui.message_entry import MessageEntry
from data.utils.math_utils import *
from data.ui.fade import Fade
from data.world.messages import create_messages
from data.ui.input_box import InputBox
from data.entities.player import Player
from data.world.location import Location
from data.world.interactable import Interactable
from data.world.item import Item
from data.ui.label import Label

BG_IMG_PATH: str = os.path.join("assets", "images", "backgrounds", "stars_background.png")
BACKGROUND_COLOUR: pygame.Color = pygame.Color(0, 0, 0)

TERMINAL_BG_IMG_PATH: str = os.path.join("assets", "images", "backgrounds", "terminal_bg.png")
SCAN_LINES_IMG_PATH: str = os.path.join("assets", "images", "scanlines.png") # TODO: still need to implement this
SPACE_AMBIENCE_PATH: str = os.path.join("assets", "music", "space_ambience1.wav")

FADE_SPEED: int = 255

AMBIENCE_VOLUME: float = 0.3
AMBIENCE_FADE_OUT_SPEED: int = 5000 # in milliseconds (1s = 1000ms)

INITIAL_MESSAGE_Y_OFFSET: int = 5

LOCATION_CONTAINER_POSITION: tuple[int, int] = (35, 26)
LOCATION_CONTAINER_SIZE: tuple[int, int] = (1211, 422)

INTERACTION_CONTAINER_POSITION: tuple[int, int] = (35, 458)
INTERACTION_CONTAINER_SIZE: tuple[int, int] = (1211, 171)

COMMAND_INPUT_SIZE: tuple[int, int] = (1222, 60)
COMMAND_INPUT_POSITION: tuple[int, int] = (29, 640)
COMMAND_INPUT_FONT_SIZE: int = 40
COMMAND_INPUT_TEXT_OFFSET_X: int = 15
COMMAND_INPUT_TEXT_OFFSET_Y: int = -5

COMMAND_LENGTH_MESSAGE: str = "Your command is too long."
COMMAND_LENGTH_POSITION: tuple[int, int] = (507, 670)
COMMAND_LENGTH_FONT_SIZE: int = 30
COMMAND_LENGTH_COLOUR: pygame.Color = pygame.Color("brown2") # should be called red2

ENDING_REVEAL_MESSAGE_ID: str = "ending_reveal"

DIRECTIONS: list[str] = ["north", "south", "east", "west"]

VERB_ALIASES: dict[str, list[str]] = {
    "go": ["go", "move", "travel", "walk", "drive", "trek", "traverse", "run", "sprint", "step", "enter", "send", "falsify", "transmit"],
    "look": ["look", "examine", "inspect", "stare", "observe", "check", "peek", "gaze", "read"],
    "take": ["take", "grab", "pickup", "yoink", "steal", "obtain", "pinch", "get", "pick", "extract", "retrieve"],
    "unlock": ["unlock", "open", "unscrew", "scan", "mount"],
    "help": ["help", "guide", "instructions", "instruction", "guides", "commands", "command", "cmd", "cmds"]
}

FILTER_WORDS: list[str] = [
    "the", 
    "at",
    "and",
    "to", 
    "on", 
    "in", 
    "up", 
    "out",
    "outwards",
    "towards", 
    "onto", 
    "forth",
    "from", 
    "into", 
    "through",
    "yourself",
    "myself",
    "a",
    "me",
    "im",
    "-",
    "[",
    "]"
]

asset_manager: AssetManager = AssetManager()


class Terminal(Scene):
    def __init__(self) -> None:
        super().__init__()
        
        self.player: Player = Player()
        
        self.fade: Fade = Fade(FADE_SPEED)
        
        self.bg_image: pygame.Surface = asset_manager.load_image("menu_bg", BG_IMG_PATH)
        self.terminal_bg_image: pygame.Surface = asset_manager.load_image("terminal_bg", TERMINAL_BG_IMG_PATH)        
        
        self.location_container: pygame.Surface = pygame.Surface(LOCATION_CONTAINER_SIZE, pygame.SRCALPHA) # pygame.SRCALPHA makes the surface transparent
        self.interaction_container: pygame.Surface = pygame.Surface(INTERACTION_CONTAINER_SIZE, pygame.SRCALPHA)
        
        self.space_ambience: pygame.mixer.Sound = asset_manager.load_sound("space_ambience", SPACE_AMBIENCE_PATH)
        
        self.command_input: InputBox = InputBox("", COMMAND_INPUT_POSITION, box_width = COMMAND_INPUT_SIZE[0], box_height = COMMAND_INPUT_SIZE[1], text_alignment = "left", font_size = COMMAND_INPUT_FONT_SIZE)
        
        self.message_index: int = 0
        
        self.message_entries: list[MessageEntry] = []
        self.sub_message_entries: list[MessageEntry] = []
        
        self.messages: dict[str, list] = create_messages()
        
        self.message_skipped: bool = False
        
        self.attempting_exit: bool = False
        
        self.command_length_warning: Label = Label(COMMAND_LENGTH_MESSAGE, COMMAND_LENGTH_POSITION, COMMAND_LENGTH_FONT_SIZE, COMMAND_LENGTH_COLOUR)
        
        self.terminal_bg_image = pygame.transform.scale(self.terminal_bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_image = pygame.transform.scale(self.bg_image, (WINDOW_WIDTH, WINDOW_WIDTH))
        self.command_input.text_offset_x = COMMAND_INPUT_TEXT_OFFSET_X
        self.command_input.text_offset_y = COMMAND_INPUT_TEXT_OFFSET_Y
        self.command_input.can_toggle = False
        self.command_input.is_toggled = True
        self.space_ambience.play(-1) # -1 loops constantly
        self.space_ambience.set_volume(AMBIENCE_VOLUME)
        self.fade.fade_in()
        self.add_main_message(self.player.current_location.message_id)
        
    def event(self, events: list[pygame.Event]) -> None:
        self.command_input.event(events)
        
        command: str | None = self.command_input.get_submitted_text()
        
        is_command_valid: bool = command is not None
        
        if is_command_valid:
            self.handle_command(command)
    
    def input(self, keys: tuple):
        if keys[pygame.K_ESCAPE]:
            if self.attempting_exit:
                return
            
            self.fade.fade_out()
            self.attempting_exit = True
        
        # skips typing animation if space is pressed
        if keys[pygame.K_SPACE]:
            self.message_skipped = True
    
    def update(self, delta: float) -> None:
        if self.message_skipped:
            self.message_skipped = False
            
            for message_entry in self.message_entries:
                message_entry.skip_animation()
        
        if self.fade.is_finished:
            if self.attempting_exit:
                self.exit()
        
        # lock the command_input until the location message is finished typing
        for message_entry in self.message_entries:
            if message_entry.is_typing:
                self.command_input.is_toggled = False
            else:
                self.command_input.is_toggled = True
        
        self.fade.update(delta)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.location_container_rect: pygame.Rect = self.location_container.get_rect(topleft=LOCATION_CONTAINER_POSITION)
        self.interaction_container_rect: pygame.Rect = self.interaction_container.get_rect(topleft=INTERACTION_CONTAINER_POSITION)
                
        screen.blit(self.bg_image)
        
        # clears the contents of the containers if nothing is being constantly being rendered (r, g, b, a)
        self.location_container.fill((0, 0, 0, 0))
        self.interaction_container.fill((0, 0, 0, 0))
        
        for entry in self.message_entries:
            entry.draw(self.location_container)
        
        for entry in self.sub_message_entries:
            entry.draw(self.interaction_container)
        
        screen.blit(self.terminal_bg_image)
        screen.blit(self.location_container, self.location_container_rect)
        screen.blit(self.interaction_container, self.interaction_container_rect)

        self.command_input.draw(screen)
        
        if self.command_input.max_characters_reached:
            self.command_length_warning.draw(screen)
        
        self.fade.draw(screen)
            
    def change_scene(self, scene) -> None:
        super().change_scene(scene)
        
        self.space_ambience.fadeout(AMBIENCE_FADE_OUT_SPEED) 
    
    # main messages appear in the bigger upper box section
    def add_main_message(self, message_id: str) -> None:
        message: list = self.messages[message_id]
        message_entry: MessageEntry = MessageEntry(message)
        
        if self.message_entries:
            previous_message_entry: MessageEntry = self.message_entries[-1]
            
            # position the newly created MessageEntry below the previous one
            message_entry.set_y(previous_message_entry.y + previous_message_entry.get_height())
        else:
            message_entry.set_y(INITIAL_MESSAGE_Y_OFFSET)
        
        self.message_entries.append(message_entry)
    
    # sub messages appear in the smaller lower box section right above the input box
    def add_sub_message(self, message_id: str) -> None:
        message: list = self.messages[message_id]
        message_entry: MessageEntry = MessageEntry(message)
        
        if self.sub_message_entries:
            previous_message_entry: MessageEntry = self.sub_message_entries[-1]
                        
            # position the newly created MessageEntry below the previous one
            message_entry.set_y(previous_message_entry.y + previous_message_entry.get_height())
        else:
            message_entry.set_y(INITIAL_MESSAGE_Y_OFFSET)
    
        self.sub_message_entries.append(message_entry)
    
    # just convenient to have
    def clear_all_messages(self) -> None:
        self.clear_main_messages()
        self.clear_sub_messages()
    
    def clear_main_messages(self) -> None:
        self.message_entries.clear()
    
    def clear_sub_messages(self) -> None:
        self.sub_message_entries.clear()
    
    # filters out words like "to", "at", "the" from the command argument
    # e.g. makes "go door" and "go out towards the door" do the same thing by stripping the argument (text after "look")
    def clean_argument(self, text: str) -> str:
        filtered_words: list[str] = []
        
        for word in text.split():
            if word not in FILTER_WORDS:
                filtered_words.append(word)
        
        # the words from the list is merged into a str with the seperator of a whitespace (ensuring a gap between words)
        return " ".join(filtered_words)
    
    # returns an Interactable of the requested name if it exists in the provided location, otherwise returns None
    def find_interactable(self, location: Location, name: str) -> Interactable | None:
        if not location.interactables:
            return
        
        interactable: Interactable | None = location.interactables.get(name)
        
        if interactable:
            return interactable
        
        # searches through a list of the Interactable objects in a location
        for interactable in location.interactables.values():
            if name in interactable.aliases:
                return interactable
        
        return None
    
    # show the related message whenever you look at an interactable
    def show_look_message(self, interactable: Interactable) -> None:
        if not interactable.message_id:
            return
        
        self.clear_sub_messages()
        self.add_sub_message(interactable.message_id)
    
    def handle_command(self, command: str) -> None:
        command = command.lower()
        
        verb, _, raw_argument = command.partition(" ")
        argument: str = self.clean_argument(raw_argument) # filters out filler words from argument
        
        location: Location = self.player.current_location
        location_interactables: dict[str, Interactable] | None = location.interactables
        
        # moving
        if verb in VERB_ALIASES["go"]:
            if argument in DIRECTIONS:
                if self.player.move(argument): # if the player moved
                    location = self.player.current_location
                    
                    self.clear_all_messages()
                    self.add_main_message(location.message_id)
                
                return
            
            interactable: Interactable | None = self.find_interactable(location, argument)
            
            if interactable:
                # interactables working as doors and moving player to locations
                if interactable.location_id:
                    message_id: str = interactable.unlock(self.player.inventory)
                    
                    self.clear_sub_messages()
                    self.add_sub_message(message_id)

                    if interactable.is_locked: 
                        self.clear_sub_messages()
                        self.add_sub_message(message_id)
                        
                        return
                    
                    if self.player.teleport(interactable.location_id): # if the player teleported
                        self.clear_all_messages()
                        # update the location description to the new location
                        self.add_main_message(self.player.current_location.message_id)
                        
                        return
                
                # helps stop confusion if someone tries to go to an interactable (which will fail and make them think something is broken) by redirecting to a look command
                self.show_look_message(interactable)
            
        elif verb in VERB_ALIASES["look"]: # looking
            if not location_interactables:
                return
            
            interactable: Interactable | None = self.find_interactable(location, argument)
            
            if interactable:
                # interactable found
                self.show_look_message(interactable)
        elif verb in VERB_ALIASES["take"]: # taking
            if not argument:
                return
            
            item: Item | None = self.player.current_location.take_item(argument)
            
            if item:
                self.player.inventory.append(item)
                self.clear_sub_messages()
                self.add_sub_message(item.take_message_id)
        elif verb in VERB_ALIASES["unlock"]: # unlocking
            if not location_interactables:
                return
            
            interactable: Interactable | None = self.find_interactable(location, argument)
            
            if interactable:
                unlock_message_id: str = interactable.unlock(self.player.inventory)
                
                if unlock_message_id == ENDING_REVEAL_MESSAGE_ID:
                    self.clear_all_messages()
                    self.add_main_message(unlock_message_id)
                    
                    return
                    
                self.clear_sub_messages()
                self.add_sub_message(unlock_message_id)
        elif verb in VERB_ALIASES["help"]: # show help
            self.clear_sub_messages()
            self.add_sub_message("command_list")
        else: # possible item-specific aliases (such as "put on" for spacesuit)
            item: Item | None = location.find_item(argument)
            
            if item:
                if not verb in item.command_aliases:
                    return

                item = location.take_item(argument)
                
                if not item:
                    return
                
                self.player.inventory.append(item)
                self.clear_sub_messages()
                self.add_sub_message(item.take_message_id)
    
    def exit(self) -> None:
        self.attempting_exit = False
        
        pygame.quit()
        sys.exit()