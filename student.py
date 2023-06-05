from human import Human
from dog import Dog
from animal import Animal
from husky import Husky


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
            super().feed(dog)
        else:
            print(f'{self.name}: Lástima :(')

    def buy_dog(self, name: str):
        self.credit = 1500
        return Husky(name)
