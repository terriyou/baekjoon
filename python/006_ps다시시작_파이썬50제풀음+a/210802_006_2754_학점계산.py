score = input()

integer = 0
under_point = 0

if len(score) == 1:
    pass
else:
    if score[0] == "A":
        integer = 4
    elif score[0] == "B":
        integer = 3
    elif score[0] == "C":
        integer = 2
    else:
        integer = 1

    if score[1] == "+":
        under_point = 3
    elif score[1] == "0":
        under_point = 0
    else:
        integer = integer -1
        under_point = 7

print(str(integer)+"."+str(under_point))