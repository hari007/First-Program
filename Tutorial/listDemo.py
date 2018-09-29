_Author_ = " HS "

cars = ["BWM", "Audi", "Benz", "Maruthi"]
empty_list = []
print(empty_list)

print('#'*30)
print(cars)
print(cars[1])

more_Cars = ["BWM", "Audi", "Benz", "Maruthi"]
more_Cars[1] = "Audi A6"
print(more_Cars)


length = len(cars)
print(length)

cars.append("Honda")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("Honda")
print(x)


y = cars.pop()  #Removes last item
print(y)
print(cars)

cars.remove("Jeep") #Removes the prticular item
print(cars)


print('#$%' *20)
slicing = cars[1:]
print(slicing)

slicing1 = cars[:]
print(slicing1)

slicing2 = cars[:2]
print(slicing2)

slicing3 = cars[1:4:3]
print(slicing3)

print("##"*10)
cars.sort()
print(cars)