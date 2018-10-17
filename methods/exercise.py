_Author_ = " HS "

states = ["Ny","Texas","California"]

def Us_tax(states, gross):
    if states == "Ny":
        fed_tax = gross * 0.1
        state_tax = gross * 0.1
        total = gross - (fed_tax + state_tax)
        print("Income for NY is " + str(total))
    elif states == "Texas":
        fed_tax = gross * 0.1
        state_tax = gross * 0.2
        total = gross - (fed_tax + state_tax)
        print("Income for Texas is " + str(total))
    else:
        fed_tax = gross * 0.1
        state_tax = gross * 0.3
        total = gross - (fed_tax + state_tax)
        print("Income for California is " + str(total))


Us_tax(states[0], 5000)