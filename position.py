import math
from typing import Tuple

from velocity import Velocity


class Position:
    """
    A basic class for simplifying position operations.
    ___

    ### Arguments
    - `x (float)`: Location in X axis.
    - `y (float)`: Location in Y axis.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_position(position: 'Position'):
        """
        Method for cloning Position objects
        ___

        ### Arguments
        `position (Position)`: Position to be cloned
        
        ### Returns
        `Position`: Cloned position object
        """
        return Position(position.x, position.y)

    def euclidean_distance_to(self, position: 'Position') -> float:
        """
        Measures the euclidean distance to given `position` argument.
    
        ### Arguments
        - `position (Position)`:  Position object to measure distance.

        ### Returns
        `float`: Euclidean distance to `position`.
        """
        distance_x, distance_y = self.axial_distances_to(position)
        return math.sqrt(pow(distance_x, 2) + pow(distance_y, 2))

    def axial_distances_to(self, position: 'Position') -> Tuple[float, float]:
        """
        Measures the axial distances to given `position` argument.
    
        ### Arguments
        - `position (Position)`: Position object to measure distance.

        ### Returns
        `tuple (float, float)`: X and Y distance to `position` object
        """
        return abs(self.x - position.x), abs(self.y - position.y)

    def shift_angular(self, angle: float, amount: float) -> None:
        """
        Shifts the position with angular arguments
    
        ### Arguments
        - `angle (float)`: Angle of the motion.
        - `amount (float)`: Amount of shifting for given angle.
        """
        delta_x = math.cos(math.radians(angle)) * amount
        delta_y = math.sin(math.radians(angle)) * amount
        self.shift_axial(delta_x, delta_y)

    def shift_axial(self, delta_x: float, delta_y: float) -> None:
        """
        Shifts the position with axial arguments.

        ### Arguments
        - `delta_x (float)`: Difference of X axis value.
        - `delta_y (float)`: Difference of Y axis value.
        """
        self.x += delta_x
        self.y += delta_y

    def as_tuple(self) -> Tuple[float, float]:
        """
        ### Returns
        `tuple (float, float)`: Position values as tuple like (x, y)
        """
        return self.x, self.y

    def __str__(self):
        return "Position: x={}, y={}".format(self.x, self.y)


def main():
    '''Created for test purposes'''
    org = Position(0, 0)
    print(org.euclidean_distance_to(Position(3, 4)))
    print(org.axial_distances_to(Position(3, 4)))


if __name__ == '__main__':
    main()
