import random

from student import Student
from human import Human
from teacher import Teacher

from animal import Animal
from dog import Dog
from husky import Husky
from chihuahua import Chihuahua
from cat import Cat

# Definir el listado de personas
student1 = Student('José Chocoy', 21)
student2 = Student('Adrian Menchu', 21)
teacher1 = Teacher('Miguel Matul', 'Sistemas Operativos')
teacher2 = Teacher('Ilia de León', 'Análisis y Diseño I')

people: list[Human] = [student1, student2, teacher1, teacher2]

# Definir el listado de mascotas
husky1 = Husky('Hachi')
chihuahua1 = Chihuahua('Chavelo')
cat1 = Cat('Gardfield', 500, True)

pets: list[Animal] = [husky1, chihuahua1, cat1]

for pet in pets:
    pet.make_sound()

# 1- Los parámetros deben coincidir o ser más abstractos
for person in people:
    animal = random.choice(pets)
    person.feed(animal)


# 2 - El tipo de retorno debe coincidir o ser más específico
dogs: list[Dog] = []
for index, person in enumerate(people):
    dog = person.buy_dog(f'Perrito {index + 1}')
    dogs.append(dog)

for dog in dogs:
    dog.bark()
