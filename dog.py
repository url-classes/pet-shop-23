from animal import Animal


class Dog(Animal):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

    def bark(self):
        print(f"{self.name}: Gua gua")

    def make_sound(self):
        self.bark()
