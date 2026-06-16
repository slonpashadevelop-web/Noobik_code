from enum import verify
from string import ascii_letters

S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
S_RUS_UPPER = S_RUS.upper()

class Person:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) !=str:
            raise TypeError("Fio must be a string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Fio must have 3 words")

        letters = ascii_letters + S_RUS + S_RUS_UPPER  # без cls.
        for s in f:
            if len(s) < 1:
                raise TypeError("Fio must have at least one letter")
            if len(s.strip(letters)) != 0:
                raise TypeError("Fio must have only letters")
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Old must be an integer")

    @classmethod
    def verify_weight(cls,w):
        if type(w) != float or w <20:
            raise TypeError("Weight must be an integer")
    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Ps must be a string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) !=4  or len(s[1]) != 6:
            raise TypeError("Ps must have 2 words")

        for p in s:
            if not p.isdigit():
                raise TypeError("Ps must have only digits")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__passport

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

p = Person('Балакирев Сергей Михайлович', 30, '1234 567866', 80.0)
p.old = 100
p.password = "1111 111111"
print(p.old)