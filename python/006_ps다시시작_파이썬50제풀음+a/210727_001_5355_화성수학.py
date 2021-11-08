n = int(input())

def goal(inpt):
    return inpt * 3

def percent(inpt):
    return inpt + 5

def sharp(inpt):
    return inpt - 7

for i in range(n):
    fomula = input().split()
    result = float(fomula[0])
    for i in range(1,len(fomula)):
        if fomula[i] == "@":
            result = goal(result)
        elif fomula[i] == "%":
            result = percent(result)
        elif fomula[i] == "#":
            result = sharp(result)
    print(format(result,".2f"))

