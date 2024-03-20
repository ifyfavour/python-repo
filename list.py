fruit = ['mango', 'orange', 'pineapple', 'banana',
         'apples', 'guava', 'watermelon', 'pears']
print(fruit)
print('---------------------------------------------------')
fruit[5] = 'grape'
print(fruit)
print('---------------------------------------------------')
fruit[5:7] = ['grapes', 'pawpaw']
print(fruit)
print('---------------------------------------------------')
fruit[5:7] = ['grapes', 'pawpaw', 'berries', 'kiwi']
print(fruit)
fruit.insert(3, 'udara')
print(fruit)
print('---------------------------------------------------')
cars = list(('G-wagon', 'Ferrari', 'IVM', 'Chevrolet', 'Bullion van', 'Tesla', 'Benz', 'BWM'))
print(cars)
print('---------------------------------------------------')
print(cars[6])
print('---------------------------------------------------')
print(cars[-4])
print('---------------------------------------------------')
print(cars[2:7])
# fruits.extends(cars)
# print(fruits)
print('---------------------------------------------------')
thistuple = ('Aba', 'Owerri', 'Enugu')
fruit.extend(thistuple)
print(fruit)
fruita = [1,2,3,(4,5,6)]
print('---------------------------------------------------')
Hairs = ['Bone straight', 'pixie curl', 'braided wig', 'bob wig', 'barbie', 'SDD Vietnum', 'full frontal wig', 'pony tail' 'skullcap']
print(Hairs)
Hairs.remove('barbie')
print(Hairs)
Hairs.pop(2)
print(Hairs)
del Hairs[-1]
