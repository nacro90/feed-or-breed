class Color:
    """
    A basic class for simplifying color operations.
    ___

    ### Arguments
    - `red (int)`: Red value of the color.
    - `green (int)`: Green value of the color.
    - `blue (int)`: Blue color of the color.
    - `alpha [int=255]`: Alpha value of the color.    

    ### Raises
    `ValueError`: If one of the (r,g,b,a) value is greater than 255 or less than 0,
    this method raises an ValueError
    """

    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        if 0 > red > 255 or 0 > green > 255 or 0 > blue > 255 or 0 > alpha > 255:
            raise ValueError(
                "Invalid subpixel value in rgb({}, {}, {})".format(red, green, blue))
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def as_tuple(self) -> tuple:
        """
        ### Returns
        `tuple (int, int, int, [int])`: Color in tuple form as (red, green, blue, [alpha])
        """
        if self.alpha is not 255:
            return self.red, self.green, self.blue, self.alpha
        else:
            return self.red, self.green, self.blue


    def __str__(self):
        s = "Color: red={}, green={}, blue={}, alpha={}"
        return s.format(self.red, self.green, self.blue, self.alpha)
