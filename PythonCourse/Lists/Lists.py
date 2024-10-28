from tkinter import Frame

Fruits = ['apple', 'orange', 'pinaple', 'pear', 'watermelon', 'raspberry',
              'strawberry', 'berries', 'banana', 'passion_fruit', 'cherry',
              'bluberry', 'lemon', 'mango', 'papaya', 'mandarine', 'grapefruit']

Fruits.remove('pear')

print(Fruits)


Fruits.append('pear')

#tworzysz nowa liste i rozszerzasz inna liste o te utworzona
New_Fruits = ['avocado', 'melon', 'peach']
Fruits.extend(New_Fruits)



#usuwasz ost elemnt z listy
item_remove = Fruits.pop()
print(f'removed item = {item_remove}')

#dodajesz element
print(Fruits)
Fruits.append('melon')

list_type = type(Fruits)
nmbr_of_list = len(Fruits)
print(f'Lista o nazwie Fruits to typ = {list_type} jest tam {nmbr_of_list} elementow')




