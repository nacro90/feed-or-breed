from typing import Tuple

class Size:
    """
    A basic class for simplifying size operations.
    ___
    
    ### Arguments
    - `width (int)`: Width of the size.
    - `height (int)`: Height of the size.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def as_tuple(self) -> Tuple[int, int]:
        """
        ### Returns
        `tuple (int, int)`: Size in tuple form as (width, height)
        """
        return self.width, self.height

    def __str__(self):
        return "Size: width={:4}, height={:4}".format(self.width, self.height)
