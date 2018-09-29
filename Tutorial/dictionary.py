_Author_ = " HS "

car = {'make': 'BMW', 'model': '550i', 'year': '2015'}
print(car)

print(car['make'])

print('$*' * 20)
d = {}

d['one'] = 1
d['two'] = 2
print(d)

d['two'] = 5
print(d)

print('**' *30)

cars2 = {'BMW1.1' : {'BWM2.1' : 'BMW2.2', 'BMW2.3' : 'BMW2.4'}, 'BMW1.2' : {'BWM2.5' : 'BMW2.6', 'BMW2.7' : 'BMW2.8'} }
print(cars2['BMW1.1']['BMW2.3'])

cars3 = {'BMW' : {'model' : '550i', 'year' : '2016'}, 'Benz' : {'model' : '550i', 'year' : '2016', 'owner' : ' Bharath Benz'}}
print('The cars are: ' + cars3 ['Benz']['owner'])

print('$*' * 20)

car = {'make': 'BMW', 'model': '550i', 'year': '2015'}
cars3 = {'BMW' : {'model' : '550i', 'year' : '2016'}, 'Benz' : {'model' : '550i', 'year' : '2016', 'owner' : ' Bharath Benz'}, 'Honda' : 'Honda City'}

print(car.keys())
print(car.values())
print(car.items())
print('$*' * 20)
print('$*' * 20)
print('$*' * 20)
print(cars3.keys())
print(cars3.values())
print(cars3.items())

car3_copy = cars3.copy()
print('$*' * 20)
print('$*' * 20)
print('$*' * 20)

print(car)
car.pop('model')
print(car)
car.clear()
print(car)

car = {'make': 'BMW', 'model': '550i', 'year': '2015'}

