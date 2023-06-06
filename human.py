from animal import Animal
from credit_error import CreditError
from dog import Dog
from husky import Husky
from chihuahua import Chihuahua


class Human:
    def __init__(self, name: str):
        self.name = name
        self.credit = 50.0

    def feed(self, dog: Dog):
        print(f"{self.name}: Voy a alimentar a {dog.name}")
        dog.eat()
        dog.make_sound()

    def buy_dog(self, name: str) -> Dog:
        if self.credit < 500:
            raise ArithmeticError()

        print(f"{self.name}: Voy a comprar un perro")
        if self.credit >= 1500.00:
            self.credit -= 1500
            return Chihuahua(name)
        elif 1000.00 <= self.credit < 1500:
            self.credit -= 1000
            return Husky(name)
        else:
            self.credit -= self.credit
            return Dog(name, self.credit, 'M')
