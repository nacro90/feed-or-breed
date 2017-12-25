import pygame
from pygame import gfxdraw

from moveable import Moveable
from renderable import Renderable

from velocity import Velocity
from position import Position
from size import Size
from color import Color

class Snake(Moveable, Renderable):
    """
    Class for simplify the tracking, manipulating, controlling the snakes.
    ___

    ### Arguments
     - `initial_position (Position)`: Initial position of the snake.
     - `initial_velocity [Velocity=Velocity(.0, .0)]`: Initial velocity of the created snake.
     - `max_velocity [float=20.0]`: Max velocity that snake can get.
     - `color (Color=Color(250,250,250))`: Color of the food.
     - `max_health [float=100.0]`: Max health value that snake can has
     - `current_health [float=None]`: Current health of the snake. (-1) for max initial health.
    """

    def __init__(self, initial_position: Position, 
                 initial_velocity: Velocity = Velocity(.0, .0), 
                 max_velocity: float = 20.0, size: Size = Size(20, 20), 
                 color: Color = Color(254, 206, 168),
                 max_health: float = 100.0, 
                 current_health: float = None):
        Moveable.__init__(self, initial_position, max_velocity, initial_velocity)
        Renderable.__init__(self)

        self.size = size
        self.color = color
        self.max_health = max_health
        if current_health is None:
            self.current_health = max_health
        else:
            self.current_health = current_health

        self.length = 1

    def _move(self, fps: int):
        """
        Moves the snake considering the FPS value.
        ___

        ### Arguments
         - `fps`: The FPS(Frames per Second) value of the game
        """
        diff_x, diff_y = self.velocity.axial_motion()
        self.position.x += diff_x / fps
        self.position.y += diff_y / fps

    def _draw(self, surface: pygame.surface.Surface, fps: int):
        """
        Renders the snake considering the FPS value.
        ___

        ### Arguments
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps`: The FPS (Frames per Second) value of the game
        """
        gfxdraw.aacircle(surface, int(self.position.x), int(self.position.y),
                         int(self.size.width / 2), self.color.as_tuple())
        gfxdraw.filled_circle(
            surface, int(self.position.x), int(self.position.y), int(self.size.width / 2), self.color.as_tuple())
