from size import Size

class Renderable:
    """
    An abstract class for storing properties of renderable objects in the game
    ___
    
    ### Paramaters
     - `visible [bool=True]`: Visibility of object
    """

    def __init__(self, visible: bool = True):
        self.visible = visible

    def render(self, surface, fps) -> None:
        """
        Renders the object considering the properties of Renderable super class.

        __Must ***NOT*** be implemented!__
        ___
        
        ### Arguments
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps (int)`: The FPS (Frames per Second) value of the game
        """
        if self.visible:
            self._draw(surface, fps)
        
    def _draw(self, surface, fps) -> None:
        """
        Abstract method that draws the object if necessary conditions are met in `render()`.

        __This method must be implemented in the object class to be drawn!__
        ___

        ### Arguments
         - `surface (pygame.surface.Surface)`: PyGame surface that the food will be drawn on.
         - `fps (int)`: The FPS (Frames per Second) value of the game

        ### Raises
        `NotImplementedError`: If the method called without implementation, 
                               NotImplementedError will be raised.
        """
        raise NotImplementedError(
            "Class {} doesn't implement render()".format(self.__class__.__name__))

    def area(self) -> Size:
        raise NotImplementedError(
            "Class {} doesn't implement area()".format(self.__class__.__name__))
