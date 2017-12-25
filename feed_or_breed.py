import pygame
from snake import Snake

from food import Food
from food_generator import FoodGenerator

from position import Position
from velocity import Velocity
from color import Color
from size import Size

from typing import List

SURFACE_SIZE = Size(900, 675)
BACKGROUND_COLOR = Color(42, 54, 59)
FPS = 60

def main():
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(SURFACE_SIZE.as_tuple())
    pygame.display.set_caption("Feed or Breed")

    generated_foods: List[Food] = []

    food_generator = FoodGenerator(SURFACE_SIZE, generation_rate=5, generating=True)

    snake = Snake(
        initial_position=Position(400, 400), 
        initial_velocity=Velocity(90, 100))

    terminate = False
    while not terminate:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate = True

        surface.fill(BACKGROUND_COLOR.as_tuple())
        
        snake.commit_movement(FPS)
        snake.render(surface, FPS)

        food_generator.generate_in_game_loop(generated_foods, FPS)
        for food in generated_foods:
            if food.is_alive():
                food.render(surface, FPS)
            else:
                generated_foods.remove(food)
        
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()

pygame.quit()
quit()
