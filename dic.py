car ={
    'brand':'toyota',
    'model':'spider',
    'year':2020,
    'color': ['ash','red', 'black']
}
print(car)
print(car['brand'])
print(car.get('color'))
print(car.keys())
car['year'] = 2025
print(car)
print(car.values())
print(car.items())
car['model'] = 'camry'
print(car)
# if 'color' in car:
#     print(True)
# car .update({'engine':'v6'})
# print(car)
# car.pop('color')
# print(car)
# # car .popitem('color')
# print(car)
# del car
# print(car)
 
# to loop through the keys
for x in car:
    print([x])
    
#to loop through values
for x in car:
    print(car[x])

for c in car.values():
    print(c)
for y in car.items():
    print(y)
for i in car.items():
    print(i)
carr = {'brand':'Lexus',}
carr = car.copy()
print(carr)

python_class = {
    'student1':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student2':{
        'name':'Justina',
        'age':12,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student3':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student4':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student5':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student6':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student7':{
        'name':'John',
        'age':17,
        'course':'AI/ML',
        'complexion': 'fair'
    },
    'student8':{
        'name':'Roy',
        'age':22,
        'course':'money',
        'complexion': 'caramel'
    }
}

print(python_class['student5']['name'])
for x in python_class.items():
    print(x)