from dog import Dog


class Husky(Dog):
    def __init__(self, name: str):
        super().__init__(name, 1000.00, 'L')

    def spin(self):
        print(f'{self.name}: Estoy girando')
