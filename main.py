class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        print(self.name, self.age, self.breed)

    def birthday(self):
        self.age += 1
        print(f'{self.name} is {self.age} years old')

d = Dog("Рекс", 3, "Овчарка")
d.birthday()
d.birthday()