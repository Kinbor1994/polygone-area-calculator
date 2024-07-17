# Polygon Area Calculator

This project demonstrates the use of object-oriented programming (OOP) in Python to create a `Rectangle` class and a `Square` class. The `Square` class is a subclass of `Rectangle`, inheriting its methods and attributes. This project covers the basic geometric operations for these shapes.

## Classes

### Rectangle

The `Rectangle` class is used to create and manipulate rectangle shapes.

#### Methods

- **`__init__(self, width, height)`**: Initializes a rectangle with the specified width and height.
- **`__str__(self)`**: Returns a string representation of the rectangle.
- **`__repr__(self)`**: Returns an official string representation of the rectangle.
- **`set_width(self, new_width)`**: Sets the width of the rectangle.
- **`set_height(self, new_height)`**: Sets the height of the rectangle.
- **`get_area(self)`**: Returns the area of the rectangle.
- **`get_perimeter(self)`**: Returns the perimeter of the rectangle.
- **`get_diagonal(self)`**: Returns the length of the diagonal of the rectangle.
- **`get_picture(self)`**: Returns a string representation of the rectangle using lines of "*". If the width or height is larger than 50, returns "Too big for picture.".
- **`get_amount_inside(self, other)`**: Returns the number of times the passed shape (another rectangle or a square) can fit inside the current rectangle.

### Square

The `Square` class is a subclass of `Rectangle` and is used to create and manipulate square shapes.

#### Methods

- **`__init__(self, side)`**: Initializes a square with the specified side length.
- **`__str__(self)`**: Returns a string representation of the square.
- **`set_side(self, new_side)`**: Sets the side length of the square, updating both width and height.
- **`set_width(self, new_width)`**: Sets the width of the square (also updates height).
- **`set_height(self, new_height)`**: Sets the height of the square (also updates width).

## Usage

Here's an example of how to use the `Rectangle` and `Square` classes:

```python
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
```
