import math

from typing import Tuple
class Velocity:
    """
    A basic class for simplifying velocity operations.
    ___
    
    ### Arguments
    - `angle (float)`: Angle of motion __in degrees__.
    - `coefficent (float)`: Velocity coefficent of motion (_Pixels per Second_).
    """
    def __init__(self, angle: float, coefficent: float) -> Tuple[float, float]:
        self.angle = angle % 360
        self.coefficent = coefficent

    def axial_motion(self) -> Tuple[float, float]:
        """
        Calculates axial motion.
        ___
        ### Returns
        `tuple (float, float)`: Velocity tuple in X and Y axis as (velocity_x, velocity_y)
        """
        velocity_x = math.cos(math.radians(self.angle)) * self.coefficent
        velocity_y = math.sin(math.radians(self.angle)) * self.coefficent
        
        return velocity_x, velocity_y

    @staticmethod
    def calculate_angle(x: int, y: int) -> float:
        """
        Calculates the angle of triangle that have edge lengths of `x` and `y`

        ### Arguments
         - `x (int)`: Horizontonal edge of triangle
         - `y (int)`: Horizontonal edge of triangle
        
        ### Returns
        `float`: Calculated angle **in degrees**
        """
        if x == 0:
            if y >= 0:
                return 90
            else: 
                return 270
        elif y == 0:
            if x >= 0:
                return 0
            else:
                return 180

        angle = abs(math.degrees(math.atan(y / x)))

        if x > 0 and y > 0:
            return angle
        elif x < 0 and y > 0:
            return 180 - angle
        elif x > 0 and y < 0:
            return 360 - angle
        elif x < 0 and y < 0:
            return 180 + angle

    def __str__(self):
        return "Velocity: angle={}, coefficent={}".format(self.angle, self.coefficent)

def main():
    """ Created for test purposes """
    print(Velocity.calculate_angle(3, 3))

if __name__ == '__main__':
    main()
