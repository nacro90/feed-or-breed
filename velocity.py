import math

from typing import Tuple
class Velocity:
    """
    A basic class for simplifying velocity operations.
    ___
    
    ### Parameters
    - `angle (float)`: Angle of motion __in degrees__.
    - `coefficent (float)`: Velocity coefficent of motion (_Pixels per Second_).
    """
    def __init__(self, angle: float, coefficent: float) -> Tuple[float, float]:
        self.angle = angle
        self.coefficent = coefficent

    def axial_motion(self):
        """
        Calculates axial motion.
        ___
        ### Returns
        `tuple (float, float)`: Velocity tuple in X and Y axis as (velocity_x, velocity_y)
        """
        velocity_x = math.cos(math.radians(self.angle)) * self.coefficent
        velocity_y = math.sin(math.radians(self.angle)) * self.coefficent
        
        return velocity_x, velocity_y
