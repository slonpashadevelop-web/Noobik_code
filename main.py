class Car:

    def __init__(self, brand):
        self.__brand = brand
        self.__speed = 0

    @classmethod
    def __check_amount(cls, amount):
        return type(amount) in [int, float] and amount > 0

    def accelerate(self, amount):
        if self.__check_amount(amount):
            self.__speed += amount
        else:
            raise ValueError("Not a valid amount")
    def brake(self, amount):
        if self.__check_amount(amount):
            self.__speed = max(0, self.__speed - amount)
        else:
            raise ValueError("Not a valid amount")

    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand

car = Car("Toyota")
print(car.get_brand())
print(car.get_speed())
car.accelerate(60)
print(car.get_speed())
car.brake(20)
print(car.get_speed())
car.brake(999)
print(car.get_speed())
car.accelerate("fast")