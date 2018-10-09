_Author_ = " HS "

l1 = [1, 2, 3]

l2 = [1, 2, 3, 4, 5, 6, 7]

for a,b in zip(l1,l2):
    if (a >= b):
        print(a)
    else:
        print(b)