import random

import factor as f

from food import Food
from size import Size
from position import Position

from typing import List


class FoodGenerator:
    """
    Class for generating random foods manually and automatically.
    ___

    ### Arguments
     - `surface_size (Size)`: Size of the pygame surface object.
     - `generation_rate [float=1]`: Number of foods to be generated in one second.
     - `generating [bool=False]`: On/off switch for generating foods.
    """

    def __init__(self, surface_size: Size, generation_rate: float = 1, generating: bool = False):
        self.surface_size = surface_size
        self.generation_rate = generation_rate
        self.generating = generating
        self.frame_counter = 0

    def generate_single_food(self):
        """
        Generates single food in game.
        ___

        ### Returns
        `Food`: Generated food.
        """
        position = Position(random.randint(0, self.surface_size.width - 1),
                            random.randint(0, self.surface_size.height - 1))
        return Food(position)

    def generate_foods(self, surface_size: Size, n_foods: int = 1):
        """
        Generates multiple foods at once.
        ___

        ### Parameters
         - `n_foods (int)`: Number of foods to be generated.

        ### Returns
        `List[Food]`: Generated foods.
        """
        generated_foods = []

        for _ in range(n_foods):
            generated_foods.append(self.generate_single_food())

        return generated_foods

    def generate_in_game_loop(self, food_bucket: List[Food], fps: int):
        """
        As the game time goes on, this method generates foods one by one in game loop.
        The generated foods are returned via `food_bucket` argument.
        ___

        ## Arguments
         - `food_bucket (List[Food])`: The list to return the generated foods.
         - `fps`: The FPS (Frames per Second) value of the game
        """
        if self.frame_counter > fps / self.generation_rate / f.TIME_FACTOR:
            food = self.generate_single_food()
            food_bucket.append(food)
            self.frame_counter -= fps / self.generation_rate / f.TIME_FACTOR

        self.frame_counter += 1

        
