from dog import Dog


class Chihuahua(Dog):
    def __init__(self, name: str):
        super().__init__(name, 1500.00, 'XXS')

    def dance(self):
        print(f'{self.name}: Estoy bailando')
