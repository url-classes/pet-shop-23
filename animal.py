from abc import abstractmethod


class Animal:
    def __init__(self, name: str, price: float):
        self.name = name
        self.energy = 50
        self.price = price

    def eat(self):
        print(f"{self.name}: Estoy comiendo...")
        self.energy += 10

    def play(self):
        if self.energy >= 10:
            print(f"{self.name}: Estoy jugando...")
            self.energy -= 10
        else:
            print(f"{self.name}: Estoy cansado.")

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError
