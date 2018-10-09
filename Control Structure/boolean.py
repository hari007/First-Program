_Author_ = " HS "

and_output1 = (10 == 10) and (10>9)
print(and_output1)

and_output2 = (10 != 10)
print(and_output2)

or_output = (10 == 10) or (9>10)
print(or_output)

not_output = not (10 == 10)
print(not_output)

print(not (not_output))



"""

************* Order of Precedence ******************
1. Not
2. And
3. OR
"""

boolean_order1 = True or not True and False
print()
print(boolean_order1)

