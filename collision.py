from typing import List, Tuple

from bubble import Bubble
from food import Food
from position import Position
from renderable import Renderable


class Collision():
    """
    Class for simplify managing and tracing the collisions between the objects.
    ___

    ### Arguments
     - `object_1 (Renderable)`: A renderable object.
     - `object_2 (Renderable)`: Another renderable object.
     - `position (Position)`: Position of the collision
    """
    def __init__(self, object_1: Renderable, object_2: Renderable, position: Position):
        self.object_1 = object_1
        self.object_2 = object_2
        self.position = position

    def __str__(self):
        return "Collision at {} between {} and {}".format(
            self.position, self.object_1, self.object_2)

    def __repr__(self):
        return "Collision: object_1=({}), object_2=({}), position={}".format(
            self.object_1, self.object_2, self.position)


class CollisionDetector:
    def __init__(self):
        pass

    def detect_feeding(self, bubbles: List[Bubble], foods: List[Food]) -> Tuple[Collision, ...]:
        collisions: List[Collision] = []
        for bubble in bubbles:
            for food in foods:
                distance = bubble.position.euclidean_distance_to(food.position)
                if distance <= bubble.radius + food.radius:
                    collision_position = Position.middle_of(
                        bubble.position, food.position)
                    collision = Collision(bubble, food, collision_position)
                    collisions.append(collision)
        return tuple(collisions)

    def detect_breeding(self):
        pass

    def detect_attacking(self):
        pass
