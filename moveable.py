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
     - `pinned [bool=True]`: Represents whether the object is not moveable or not. Can be used for temporary stops.
    """

    def __init__(self, initial_position: Position, max_velocity: float,
                 initial_velocity: Velocity = Velocity(.0, .0), pinned: bool = True):
        self.position = initial_position
        self.max_velocity = max_velocity
        self.velocity = initial_velocity
        self.pinned = pinned

    def move(self, fps: int) -> Position:
        """
        Moves the object according to its velocity and value of the frames per second
        
        **This method must be implemented**
        ___

        ### Parameters
         - `fps (int)`: Value of frames per second of the game

        ### Returns
        `Position`: New position of the object after the movement

        ### Raises
        `NotImplementedError`: If the method called without implementation, 
                               NotImplementedError will be raised.
        """
        raise NotImplementedError(
            "Class {} doesn't implement move()".format(self.__class__.__name__))

def main():
    """ Created for test purposes """

if __name__ == '__main__':
    main()
