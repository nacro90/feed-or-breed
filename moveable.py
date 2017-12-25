from position import Position
from velocity import Velocity

class Moveable():
    """
    An abstract class for storing properties of moveable objects in the game
    ___
    
    ### Paramaters
     - `initial_position (Position)`: Initial position of moveable object.
     - `max_velocity (float)`: The highest speed that the moveable object can be moving obround
     - `initial_velocity [Velocity=Velocity(.0, .0)]`: The velocity of the object when its created.
     - `pinned [bool=False]`: Represents whether the object is not moveable or not. Can be used for temporary stops.
    """

    def __init__(self, initial_position: Position, max_velocity: float,
                 initial_velocity: Velocity = Velocity(.0, .0), pinned: bool = False):
        self.position = initial_position
        self.max_velocity = max_velocity
        self.velocity = initial_velocity
        self.pinned = pinned

    def commit_movement(self, fps: int):
        """
        Process the movement of the object considering the properties of Moveable super class.

        __Must ***NOT*** be implemented!__
        ___
        
        ### Arguments
         - `fps (int)`: The FPS (Frames per Second) value of the game
        """
        if self.pinned is not True:
            self._move(fps)


    def _move(self, fps: int):
        """
        Moves the object according to its velocity and value of the frames per second
        
        **This method must be implemented**
        ___

        ### Arguments
         - `fps (int)`: Value of frames per second of the game

        ### Raises
        `NotImplementedError`: If the method called without implementation, 
                               NotImplementedError will be raised.
        """
        raise NotImplementedError(
            "Class {} doesn't implement move()".format(self.__class__.__name__))

    def set_velocity_for_target(self, target: Position):
        diff_x = target.x - self.position.x
        diff_y = target.y - self.position.y
        self.velocity.angle = Velocity.calculate_angle(diff_x, diff_y)
        

def main():
    """ Created for test purposes """

if __name__ == '__main__':
    main()
