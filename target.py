import pygame
from pygame import gfxdraw

from renderable import Renderable

from position import Position
from color import Color

class Target(Renderable):
    """
    Class for simplify tracking mouse movement and passing to moveables
    ___

    ### Arguments
     - `position (Position)`: Position of the target
     - `size (float)`: Size of each line of crosshair
     - `visible [bool=False]`: Specifies whether render the target or not. 
    """

    def __init__(self, position: Position, visible: bool = False, size: int = 20):
        Renderable.__init__(self, visible=visible)
        self.position = position
        self.size = size

    def _draw(self, surface, fps):
        gfxdraw.hline(
            surface, 
            int(self.position.x - self.size / 2),
            int(self.position.x + self.size / 2),
            int(self.position.y),
            Color(255, 255, 255).as_tuple())
        gfxdraw.vline(
            surface, 
            int(self.position.x), 
            int(self.position.y - self.size / 2),
            int(self.position.y + self.size / 2),
            Color(255, 255, 255).as_tuple())
