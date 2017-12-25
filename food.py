import pygame
from pygame import gfxdraw

from size import Size
from position import Position
from color import Color
from renderable import Renderable


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
    EXISTENCE_LENGTH = 5.0

    def __init__(self, position: Position, size: Size = Size(10, 10),
                 color: Color = Color(250, 250, 250, 255)):
        Renderable.__init__(self)

        self.size = size
        self.position = position
        self.color = color
        self.remaining_life = self.EXISTENCE_LENGTH

    def draw(self, surface: pygame.surface.Surface, fps: int):
        """
        Renders the food considering FPS value.
        ___

        ### Parameters
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps`: The FPS (Frames per Second) value of the game
        """
        gfxdraw.aacircle(surface, self.position.x, self.position.y, self.radius(), self.color.as_tuple())
        gfxdraw.filled_circle(surface, self.position.x, self.position.y, self.radius(), self.color.as_tuple())
        self.remaining_life -= 1 / fps

    def is_alive(self) -> bool:
        """
        ### Returns
        `bool`: Whether remaining life is less than zero or not
        """
        return bool(self.remaining_life > 0)


    def radius(self) -> int:
        """
        ### Returns 
        `int`: Radius of the food as integer
        """
        return int(self.size.width / 2)

    def __str__(self):
        s = "Food: position={}, size={}, color={}, remaining_life={}, visible={}"
        return s.format(self.position.as_tuple(),
                        self.size.as_tuple(),
                        self.color.as_tuple(),
                        self.remaining_life,
                        self.visible)
