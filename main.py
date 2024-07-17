class Rectangle:
    """Represents a rectangle shape."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: A string in the format 'Rectangle(width=x, height=y)'.
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        """
        Returns an official string representation of the Rectangle instance.

        Returns:
            str: A string in the format 'Rectangle(width=x, height=y)'.
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        """
        Sets the width of the rectangle.

        Args:
            new_width (int): The new width of the rectangle.
        """
        self.width = new_width

    def set_height(self, new_height):
        """
        Sets the height of the rectangle.

        Args:
            new_height (int): The new height of the rectangle.
        """
        self.height = new_height

    def get_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Calculates the diagonal length of the rectangle.

        Returns:
            float: The diagonal length of the rectangle.
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Returns a string representation of the rectangle using lines of "*".

        Returns:
            str: A string representation of the rectangle with "*" characters.
            If the width or height is larger than 50, returns "Too big for picture.".
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ("*" * self.width + "\n") * self.height
        return picture

    def get_amount_inside(self, other):
        """
        Calculates how many times another shape can fit inside this rectangle.

        Args:
            other (Rectangle or Square): Another shape to fit inside this rectangle.

        Returns:
            int: The number of times the other shape can fit inside this rectangle.
        """
        return self.get_area() // other.get_area()

class Square(Rectangle):
    """Represents a square shape, which is a special case of a rectangle."""

    def __init__(self, side):
        """
        Initializes a Square instance with the specified side length.

        Args:
            side (int): The side length of the square.
        """
        super().__init__(width=side, height=side)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string in the format 'Square(side=x)'.
        """
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        """
        Sets the side length of the square, updating both width and height.

        Args:
            new_side (int): The new side length of the square.
        """
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        """
        Sets the width of the square, which also updates the height.

        Args:
            new_width (int): The new width of the square.
        """
        self.set_side(new_width)

    def set_height(self, new_height):
        """
        Sets the height of the square, which also updates the width.

        Args:
            new_height (int): The new height of the square.
        """
        self.set_side(new_height)

# Usage example
rect = Rectangle(10, 5)
print(rect.get_area())  # 50
rect.set_height(3)
print(rect.get_perimeter())  # 26
print(rect)  # Rectangle(width=10, height=3)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())  # 81
sq.set_side(4)
print(sq.get_diagonal())  # 5.656854249492381
print(sq)  # Square(side=4)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8
