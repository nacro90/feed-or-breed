import math
from typing import List

import pygame

import factor as f
from color import Color
from food import Food
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
    DEFAULT_MAX_VELOCITY: float = 500.0
    DEFAULT_MAX_FRICTION: float = DEFAULT_MAX_VELOCITY / 2
    DEFAULT_RADIUS: float = 10.0
    DEFAULT_COLOR: Color = Color(254, 206, 168)
    DEFAULT_MAX_HEALTH: float = 100.0 
    DEFAULT_JOINT_GAP: float = 10.0

    def __init__(self,
                 position: Position,
                 velocity: Velocity = Velocity(.0, .0),
                 max_velocity: float = DEFAULT_MAX_VELOCITY,
                 max_friction: float = DEFAULT_MAX_FRICTION,
                 radius: float = DEFAULT_RADIUS,
                 color: Color = DEFAULT_COLOR,
                 max_health: float = DEFAULT_MAX_HEALTH,
                 current_health: float = None):

        Moveable.__init__(self, position, max_velocity, velocity)
        Renderable.__init__(self)

        self.max_friction = max_friction
        self.radius = radius
        self.color = color
        self.max_health = max_health
        if current_health is None:
            self.current_health = max_health
        else:
            self.current_health = current_health

        self.food_counter = 0

    
    def eaten(self, food: Food):
        self.food_counter += 1
        self.radius = math.sqrt((food.area() + self.area()) / math.pi)


    def set_velocity_for_target(self, 
                                target: Position, 
                                deceleration_easing: float = 40, 
                                friction_easing: float = 100) -> None:
        """
        Calculates and sets the angle and the coefficent of moveable's velocity.
        
        Deceleration is used with the equasion of:
        ```
        m = Max velocity of moveable  
        d = Distance to target  
        e = Easing coefficent

        ( (m * e / -(d + e)) + m )
        ```
        This equasion diverges to max speed of the bubble.

        Friction increase is used with the equasion of hyperbolic tangent
        formula with specific divergence value.
        ``` 
        m = Max friction value of bubble.
        f = Number of foods those have eaten by the bubble
        e = Friction increase easing.

        ( m * (exp(f/e) - exp(-f/e)) / (exp(f/e) + exp(-f/e)) )
        ```
        ___

        ### Arguments
         - `target (Position)`: Target position.
         - `easing [float=40]`: Deceleration easing coefficent
        """
        diff_x = target.x - self.position.x
        diff_y = target.y - self.position.y
        self.velocity.angle = Velocity.calculate_angle(diff_x, diff_y)

        # Deceleration
        m = self.max_velocity
        d = self.position.euclidean_distance_to(target)
        e = deceleration_easing
        calculated_coefficent = (m * e / -(d + e)) + m

        # Friction
        m = self.max_friction
        f = self.food_counter
        e = friction_easing
        decreasing_friction = \
            m * (
                (math.exp(f / e) - math.exp(-f / e)) /
                (math.exp(f / e) + math.exp(-f / e))
            )

        self.velocity.coefficent = calculated_coefficent - decreasing_friction


    def _move(self, fps: int):
        """
        Moves the bubble considering the FPS value.
        ___

        ### Arguments
         - `fps`: The FPS(Frames per Second) value of the game
        """
        diff_x, diff_y = self.velocity.axial_motion()
        self.position.x += diff_x / fps * f.TIME_FACTOR
        self.position.y += diff_y / fps * f.TIME_FACTOR


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
                                int(self.radius),
                                self.color.as_tuple())

        pygame.gfxdraw.filled_circle(surface,
                                     int(self.position.x),
                                     int(self.position.y),
                                     int(self.radius),
                                     self.color.as_tuple())

    def area(self):
        return math.pi * pow(self.radius, 2)

    def rectangular_size(self):
        return Size(self.radius * 2, self.radius * 2)


def main():
    """ Created for test purposes """


if __name__ == '__main__':
    main()
