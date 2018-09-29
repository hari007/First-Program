_Author_ = " HS "


#finding the index
first = "nyc"[0] #index starts from 0. So output will be n.
print(first)

city = "sfo"
var1 = city[1]
print(var1)


string1 = "These are string in buit operations"

print(string1.upper())
print(string1.lower())
print(string1.__len__())  #find the length
print(len(string1))

print(string1 + str(2))  #concatenation


print("Hello " + "World")

print(first + " " + city)

a = "1abc2ABC3abc"
print(a.replace('abc','ABC', 2)) #Here it replaces small case abc to Upper case.


sub = a[1:6] #it starts from 1 but doesn't include 6
step = a[1:6:2] #here i to 6 is the range. every 2nd word is printed

print(sub)
print(step)

string2 = "This is a string"

print('*******************')
print(string2[:]) #Print entire string
print(string2[1:]) #Prints from the specified position
print(string2[:6]) #Prints till the specified position
print(string2[-1]) #Print the last chacter
print(string2[-2]) #Prints the 2 character from the end of the string


print('******************')
print(string2[:-2])
print(string2[:len(string2)-3])
print(string2[::3])
print(string2[::-3])