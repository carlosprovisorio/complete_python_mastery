# Class: blueprint for creating new objects
# Object: instance of a class


# Class: Human
# Objects: John, Mary, Jack


class Point:
    default_color = "red"

    def __init__(self, x, y):  # Self is a reference to the current object
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(point.default_color)
point.draw()

another = Point(3, 4)
another.draw()
