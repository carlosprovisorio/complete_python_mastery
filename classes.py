# Class: blueprint for creating new objects
# Object: instance of a class


# Class: Human
# Objects: John, Mary, Jack


class Point:
    def __init__(self, x, y):  # Self is a reference to the current object
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
