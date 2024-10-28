#tuple
#krotki
from multiprocessing.util import ForkAwareLocal
from pickle import FALSE

Fruits = ['apple', 'orange', 'pinaple', 'pear', 'watermelon', 'raspberry',
              'strawberry', 'berries', 'banana', 'passion_fruit', 'cherry',
              'bluberry', 'lemon', 'mango', 'papaya', 'mandarine', 'grapefruit']

My_Tuple_1 = (1, 3, 5, 'Cos', 43.534, 'kupa', 'kolejne_cos', 4235.5235, 'blabla_bleee')

Fruits_type = type(Fruits)
Tuple_type = type(My_Tuple_1)

print(f'Fruits to {Fruits_type}\n'
      f'My_Tuple_1 to {Tuple_type}')

print(False and True)
print(True or False)

