_Author_ = " HS "

a = 10
def test(a):
    print("The value of local 'a' is "+ str(a))
    a = 2
    print("The value of local 'a' is "+ str(a))

print("Value of Global 'a' is " + str(a))
test(a)
print("Value of Global 'a' is " + str(a))

a = 10
def test():
    global a
    print("The value of local 'a' is "+ str(a))
    a = 2
    print("The value of local 'a' is "+ str(a))

print("Value of Global 'a' is " + str(a))
test()
print("Value of Global 'a' is " + str(a))
