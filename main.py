import random

from credit_error import CreditError
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
student1.feed(husky1)
student2.feed(cat1)

# teacher1.feed(husky1)
# teacher2.feed(chihuahua1)


# 2 - El tipo de retorno debe coincidir o ser más específico
dogs: list[Dog] = []

student1.credit = 1500
dogs.append(student1.buy_dog('Bruno'))
student2.credit = 1500
dogs.append(student2.buy_dog('Pinky'))

# teacher1.credit = 1000
# dogs.append(teacher1.buy_dog('Buster'))


for dog in dogs:
    dog.bark()

# 3 - Se deben lanzar excepciones del mismo tipo o subtipos de la base

try:
    student1.credit = 300
    student1.buy_dog('Firu')
except ArithmeticError as e:
    print(e)

# try:
#     teacher1.credit = 800
#     teacher1.buy_dog('Dash')
# except ArithmeticError as e:
#     print(e)
