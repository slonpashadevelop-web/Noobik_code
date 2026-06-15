class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
         self.x = x
         self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("Доступа не булет")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

pt1 = Point(1, 2)
pt2 = Point(10, 20)