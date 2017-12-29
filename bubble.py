from typing import List

import pygame

from color import Color
from moveable import Moveable
from position import Position
from renderable import Renderable
from size import Size
from velocity import Velocity


class Bubble(Moveable, Renderable):
    """
    Class for simplify the tracking, manipulating, controlling the bubbles.
    ___

    ### Arguments
     - `position (Position)`: Initial position of the bubble.
     - `velocity [Velocity=Velocity(.0, .0)]`: Initial velocity of the created bubble.
     - `max_velocity [float=20.0]`: Max velocity that bubble can get.
     - `color (Color=Color(250,250,250))`: Color of the food.
     - `max_health [float=100.0]`: Max health value that bubble can has
     - `current_health [float=None]`: Current health of the bubble. (None) for max initial health.
     - `joint_gap [float=10.0]`: Gaps between joints
    """

    # Default values
    DEFAULT_MAX_VELOCITY: float = 300.0
    DEFAULT_SIZE: Size = Size(20, 20)
    DEFAULT_COLOR: Color = Color(254, 206, 168)
    DEFAULT_MAX_HEALTH: float = 100.0 
    DEFAULT_JOINT_GAP: float = 10.0

    def __init__(self,
                 position: Position,
                 velocity: Velocity = Velocity(.0, .0),
                 max_velocity: float = DEFAULT_MAX_VELOCITY,
                 size: Size = DEFAULT_SIZE,
                 color: Color = DEFAULT_COLOR,
                 max_health: float = DEFAULT_MAX_HEALTH,
                 current_health: float = None):

        Moveable.__init__(self, position, max_velocity, velocity)
        Renderable.__init__(self)

        self.size = size
        self.color = color
        self.max_health = max_health
        if current_health is None:
            self.current_health = max_health
        else:
            self.current_health = current_health


    def _move(self, fps: int):
        """
        Moves the bubble considering the FPS value.
        ___

        ### Arguments
         - `fps`: The FPS(Frames per Second) value of the game
        """
        diff_x, diff_y = self.velocity.axial_motion()
        self.position.x += diff_x / fps
        self.position.y += diff_y / fps


    def _draw(self, surface: pygame.surface.Surface, fps: int):
        """
        Renders the bubble considering the FPS value.
        ___

        ### Arguments
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps`: The FPS (Frames per Second) value of the game
        """
        pygame.gfxdraw.aacircle(surface,
                                int(self.position.x),
                                int(self.position.y),
                                int(self.size.width / 2),
                                self.color.as_tuple())

        pygame.gfxdraw.filled_circle(surface,
                                     int(self.position.x),
                                     int(self.position.y),
                                     int(self.size.width / 2),
                                     self.color.as_tuple())



def main():
    """ Created for test purposes """


if __name__ == '__main__':
    main()
