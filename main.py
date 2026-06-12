class Point:
    color = "red"
    circle = 2

    def __init__(self, a=0 , b=0):
        self.x = a
        self.y = b

    def __del__(self):
        print("Удаление" + str(self))

    def set_coords(self, x ,y ):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt =Point()
print(pt.__dict__)