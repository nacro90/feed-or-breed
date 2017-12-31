import math

import pygame
from pygame import gfxdraw

from color import Color
from position import Position
from renderable import Renderable
from size import Size


class Food(Renderable):
    """
    Class for simplify the tracking, manipulating, controlling the foods.
    ___

    ### Arguments
     - `position (Position)`: Position of the food.
     - `size (Size=Size(50,50)`: Size of the food.
     - `color (Color=Color(250,250,250))`: Color of the food.
    """

    # Food existence length in seconds
    DEFAULT_EXISTENCE_LENGTH: float = 5.0

    DEFAULT_RADIUS: float = 5.0

    def __init__(self, position: Position, radius: float = DEFAULT_RADIUS,
                 existence_length: float = DEFAULT_EXISTENCE_LENGTH,
                 color: Color = Color(153, 184, 152, 255)):
        Renderable.__init__(self)

        self.radius = radius
        self.position = position
        self.color = color
        
        self.existence_length = self.remaining_life = existence_length

    def _draw(self, surface: pygame.surface.Surface, fps: int):
        """
        Renders the food considering the FPS value.
        ___

        ### Arguments
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps`: The FPS (Frames per Second) value of the game
        """
        gfxdraw.aacircle(
            surface, int(self.position.x), int(self.position.y),
            int(self.radius), self.color.as_tuple())
        gfxdraw.filled_circle(
            surface, int(self.position.x), int(self.position.y), 
            int(self.radius), self.color.as_tuple())
        self.remaining_life -= 1 / fps

    def is_alive(self) -> bool:
        """
        ### Returns
        `bool`: Whether remaining life is less than zero or not
        """
        return bool(self.remaining_life > 0)

    def rectangular_size(self):
        return Size(self.radius * 2, self.radius * 2)

    def area(self):
        return math.pi * pow(self.radius, 2)
