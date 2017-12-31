import math
from typing import List

import pygame

from bubble import Bubble
from collision import CollisionDetector
from color import Color
from food import Food
from food_generator import FoodGenerator
from position import Position
from size import Size
from target import Target
from velocity import Velocity

SURFACE_SIZE = Size(900, 675)
BACKGROUND_COLOR = Color(42, 54, 59)
FPS = 60

def main():
    global FPS 

    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(SURFACE_SIZE.as_tuple())
    pygame.display.set_caption("Feed or Breed")

    generated_foods: List[Food] = []

    food_generator = FoodGenerator(SURFACE_SIZE, generation_rate=10, generating=True)

    collision_detector = CollisionDetector()

    bubble = Bubble(Position(SURFACE_SIZE.width / 2, SURFACE_SIZE.height / 2))

    target = Target(Position(0, 0), visible=False)

    terminate = False
    while terminate is not True:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate = True
            elif event.type == pygame.MOUSEMOTION:
                target.position.x = event.pos[0]
                target.position.y = event.pos[1]
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 't':
                    target.visible = not target.visible
                if event.unicode == 'v':
                    bubble.visible = not bubble.visible

        surface.fill(BACKGROUND_COLOR.as_tuple())

        food_generator.generate_in_game_loop(generated_foods, FPS)
        for food in generated_foods:
            food: Food
            if food.is_alive():
                food.render(surface, FPS)
            else:
                generated_foods.remove(food)

        feeding_collisions = collision_detector.detect_feeding([bubble], generated_foods)
        for collision in feeding_collisions:
            food = collision.object_2
            generated_foods.remove(food)
            bubble.eaten(food)

        
        if target.position.euclidean_distance_to(bubble.position) < bubble.velocity.coefficent / FPS:
            bubble.position = Position.from_position(target.position)
            bubble.pinned = True
        else:
            bubble.pinned = False
            bubble.set_velocity_for_target(target.position)
            bubble.commit_movement(FPS)
        
        bubble.render(surface, FPS)

        if target is not None:
            target.render(surface, FPS)
        
        pygame.display.update()
        clock.tick(FPS) 


    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
