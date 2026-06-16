class Rectangle:

    def __init__(self, width, height):
        self.check_value(width)
        self.check_value(height)

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if self.check_value(new_width):
            self.__width = new_width
        else:
            raise ValueError("width must be greater than 0")

    @classmethod
    def check_value(cls, value):
        if type(value) == int and value > 0:
            return True
        else:
            return False

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if self.check_value(new_height):
            self.__height = new_height
        else:
            raise ValueError("height must be greater than 0")
    @property
    def area(self):
        return self.__width * self.__height

    @property
    def perimeter(self):
        return 2 * (self.__width * self.__height)


r = Rectangle(4, 5)
print(r.width)       # 4
print(r.height)      # 5
print(r.area)         # 20
print(r.perimeter)    # 18

r.width = 10
print(r.area)          # 50
