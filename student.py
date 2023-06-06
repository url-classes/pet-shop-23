from credit_error import CreditError
from human import Human
from animal import Animal
from chihuahua import Chihuahua


class Student(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def request_money(self, amount: float):
        self.credit += amount

    def feed(self, dog: Animal):
        print(f"{self.name}: ¿Puedo alimentar a {dog.name}?")
        option = input('Ingrese una opción (S/N): ')
        if option == 'S':
            dog.eat()
            dog.make_sound()
        else:
            print(f'{self.name}: Lástima :(')

    def buy_dog(self, name: str):
        if self.credit < 1500:
            raise CreditError()

        self.credit -= 1500
        return Chihuahua(name)
