from animal import Animal


class Cat(Animal):
    def __init__(self, name: str, price: float, is_friendly: bool):
        super().__init__(name, price)
        self.is_friendly = is_friendly

    def meow(self):
        print(f"{self.name}: meooow")

    def make_sound(self):
        self.meow()
