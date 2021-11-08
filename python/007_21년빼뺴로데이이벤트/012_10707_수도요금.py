inpt = [int(input()) for _ in range(5)]

def calc_a(inpt):
    return inpt[0] * inpt[4]

def calc_b(inpt):
    sang_han_calc = inpt[4] - inpt[2]
    if sang_han_calc < 0:
        result = inpt[1]
    else:
        result = inpt[1] + sang_han_calc * inpt[3]    
    return result

a_fee = calc_a(inpt)
b_fee = calc_b(inpt)

if a_fee > b_fee:
    print(b_fee)
elif a_fee < b_fee:
    print(a_fee)
else:
    print(a_fee)