import pygame
import sys
import os
import math

from data.core.asset_manager import AssetManager
from data.scenes.scene import Scene
from data.scenes.terminal import Terminal
from data.ui.label import Label
from data.ui.animated_button import AnimatedButton
from data.ui.fade import Fade

from data.core.settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH_CENTER, WINDOW_HEIGHT_CENTER, WINDOW_CAPTION

asset_manager: AssetManager = AssetManager()

# os.path.join automatically handles system-specific path formats
BG_IMG_PATH: str = os.path.join(
    "assets", "images", "backgrounds", "stars_background.png"
)
BG_SCROLL_SPEED: float = 0.15

TITLE_POSITION: tuple[int, int] = (50, 0)  # pygame unusally stores x and y as int
TITLE_COLOUR: pygame.Color = pygame.Color(227, 218, 201)
TITLE_FONT_PATH: str = os.path.join("assets", "fonts", "Redden.ttf")
TITLE_FONT_SIZE: int = 128
TITLE_SINE_AMPLITUDE: float = 1.7
TITLE_SINE_FREQUENCY: float = 0.004

CREDITS_POSITION: tuple[int, int] = (1050, 650)
CREDITS_FONT_SIZE: int = 24

BUTTON_SPACING: int = 55
BUTTON_FONT_SIZE: int = 48
BUTTON_X_OFFSET: int = 50
BUTTON_ANCHOR_POSITION: tuple[int, int] = (BUTTON_X_OFFSET, WINDOW_HEIGHT_CENTER + WINDOW_HEIGHT_CENTER // 2)

CHIME_EXIT_PATH: str = os.path.join("assets", "sounds", "chime_exit.mp3")
CHIME_LOAD_PATH: str = os.path.join("assets", "sounds", "chime_load.mp3")

FADE_SPEED: int = 255  # inversed (lower is slower, higher is faster)


class MainMenuScene(Scene):
    def __init__(self) -> None:
        super().__init__()

        # store as floats so the bg can scroll more slowly
        self.bg_x: float = 0
        self.bg_y: float = 0
        self.bg_image: pygame.Surface = asset_manager.load_image("menu_bg", BG_IMG_PATH)
        self.bg_rect: pygame.rect.Rect = self.bg_image.get_rect()
        self.fade: Fade = Fade(FADE_SPEED)

        self.attempting_exit: bool = False

        # resize before centering so centre position is not offset as scaling is done from the top left (0, 0)
        self.bg_image = pygame.transform.scale(self.bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_rect.center = (WINDOW_WIDTH_CENTER, WINDOW_HEIGHT_CENTER)

        self.title: Label = Label(WINDOW_CAPTION, TITLE_POSITION, TITLE_FONT_SIZE, TITLE_COLOUR, TITLE_FONT_PATH)
        self.credit: Label = Label("A game by Aidan Kelly", CREDITS_POSITION, CREDITS_FONT_SIZE)
        self.play_button: AnimatedButton = AnimatedButton("Play", BUTTON_ANCHOR_POSITION, BUTTON_FONT_SIZE)
        self.quit_button: AnimatedButton = AnimatedButton("Quit", (BUTTON_X_OFFSET, self.play_button.position[1] + BUTTON_SPACING), BUTTON_FONT_SIZE)

        self.fade.fade_in()

    def update(self, delta: float) -> None:
        ticks: int = pygame.time.get_ticks()
        title_sine_offset: float = math.sin(ticks * TITLE_SINE_FREQUENCY) * TITLE_SINE_AMPLITUDE

        self.bg_x -= BG_SCROLL_SPEED
        self.title.position = (TITLE_POSITION[0], TITLE_POSITION[1] + int(title_sine_offset)) # the y of the sine wave is sampled for a floating effect

        self.fade.update(delta)

        # if the x pos of the bg is less than window width inversed (-640) teleport to start
        # wasted about 4 hours getting this nonsense to work, good thing it's so important!
        if self.bg_x <= -WINDOW_WIDTH:
            self.bg_x = 0

        if self.play_button.is_pressed():
            if self.attempting_scene_change:
                return

            self.fade.fade_out()
            self.attempting_scene_change = True

        if self.quit_button.is_pressed():
            if self.attempting_exit:
                return

            self.fade.fade_out()
            self.attempting_exit = True

        # if fade isn't fading (or have just finished fading)
        if self.fade.is_finished:
            # it isnt attempting to change scene, then change scene
            if self.attempting_scene_change:
                self.change_scene(Terminal())

            # if it is attempting to exit the game, then exit
            if self.attempting_exit:
                self.exit()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.bg_image, (self.bg_x, self.bg_y))
        # add another bg img stitched after the above one to create seamless scrolling
        screen.blit(self.bg_image, (self.bg_x + WINDOW_WIDTH, self.bg_y))

        self.title.draw(screen)
        self.credit.draw(screen)
        self.play_button.draw(screen)
        self.quit_button.draw(screen)
        self.fade.draw(screen)

    def change_scene(self, scene: Scene) -> None:
        self.next_scene = scene

    def exit(self) -> None:
        self.attempting_exit = False
        pygame.quit()
        sys.exit()