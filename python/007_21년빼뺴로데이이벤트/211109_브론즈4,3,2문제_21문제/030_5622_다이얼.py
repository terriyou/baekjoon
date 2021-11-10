inpt = input()

cost = []

def calc_cost(inpt):
    ord_inpt = ord(inpt)
    result = 0
    if ord_inpt < 65:
        result = 0
    elif ord_inpt < 68:
        result = 3
    elif ord_inpt < 71:
        result = 4
    elif ord_inpt < 74:
        result = 5
    elif ord_inpt < 77:
        result = 6
    elif ord_inpt < 80:
        result = 7
    elif ord_inpt < 84:
        result = 8
    elif ord_inpt < 87:
        result = 9  
    elif ord_inpt < 91:
        result = 10
    else:
        result = 0
    return result

for i in inpt:
    cost.append(calc_cost(i))

print(sum(cost))
