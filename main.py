class BankAccount:

    def __init__(self, owner,balance ):
        self.__owner = None
        self.__balance = 0
        if self.__check_owner(owner) and self.__check_balance(balance):
            self.__balance = balance
            self.__owner = owner


    @classmethod
    def __check_owner(cls,owner):
        return type(owner) in [str]


    @classmethod
    def __check_balance(cls,balance):
        return type(balance) in [int,float] and balance > 0

    def set_owner(self, owner):
        if self.__check_owner(owner):
            self.__owner = owner
        else:
            raise ValueError('не должно бфть строкой')

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return  self.__balance

    def deposit(self,amount):
        if self.__check_balance(amount):
            self.__balance += amount
        else:
            raise ValueError(" no")

    def withdraw(self,amount):
        if self.__check_balance(amount) and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError(" no")