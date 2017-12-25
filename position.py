import math

from typing import Tuple


class Position:
    """
    A basic class for simplifying position operations.
    ___

    ### Arguments
    - `x (int)`: Location in X axis.
    - `y (int)`: Location in Y axis.
    """

    def __init__(self, x: float, y: float):
        self.x = int(x)
        self.y = int(y)

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

    def axial_distances_to(self, position: 'Position') -> Tuple[int, int]:
        """
        Measures the axial distances to given `position` argument.
    
        ### Arguments
        - `position (Position)`:  Position object to measure distance.

        ### Returns
        `tuple (int, int)`: X and Y distance to `position` object
        """
        return abs(self.x - position.x), abs(self.y - position.y)

    def as_tuple(self) -> Tuple[int, int]:
        """
        ### Returns
        `tuple (int, int)`: Position values as tuple like (x, y)
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
