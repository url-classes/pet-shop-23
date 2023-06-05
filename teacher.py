from human import Human
from husky import Husky


class Teacher(Human):
    def __init__(self, name: str, course: str):
        super().__init__(name)
        self.course = course
        self.credit = 10000.0

    def feed(self, dog: Husky):
        print(f"{self.name}: Voy a alimentar a {dog.name}")
        dog.spin()
