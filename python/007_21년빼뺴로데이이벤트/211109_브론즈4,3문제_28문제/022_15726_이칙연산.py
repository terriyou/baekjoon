inpt = list(map(int, input().split()))

ex_1 = int(inpt[0] * inpt[1] / inpt[2])
ex_2 = int(inpt[0] / inpt[1] * inpt[2])

print(ex_1 if ex_1 > ex_2 else ex_2)