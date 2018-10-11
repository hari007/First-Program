_Author_ = " HS "

def sum_num(n1, n2):
    """

    :param n1:
    :param n2:
    :return:
    """
    print(n1 + n2)


sum_num(2, 3)
sum_num(3, 5)
sum_num(7, 9)


def sum_num2(a, b):
    return a+ b


print(sum_num2(5, 15))


print('&*%' *20)

def citymetro(city):
    l = ["Kochi","Kannur", "Pala"]

    if city in l:
        return 1
    else:
        return False

X = citymetro("Kochi")

print(X)