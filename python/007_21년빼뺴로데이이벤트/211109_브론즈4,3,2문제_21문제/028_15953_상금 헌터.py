n = int(input())

def prize_2017(inpt):
    result = 0
    if inpt < 1:
        result = 0
    elif inpt < 2:
        result = 500
    elif inpt < 4:
        result = 300
    elif inpt < 7:
        result = 200
    elif inpt < 11:
        result = 50
    elif inpt < 16:
        result = 30
    elif inpt < 22:
        result = 10
    else:
        result = 0
    return result * 10000

def prize_2018(inpt):
    result = 0
    if inpt < 1:
        result = 0
    elif inpt < 2:
        result = 512
    elif inpt < 4:
        result = 256
    elif inpt < 8:
        result = 128
    elif inpt < 16:
        result = 64
    elif inpt < 32:
        result = 32
    else:
        result = 0
    return result * 10000

for i in range(n):
    inpt = list(map(int, input().split()))
    result = prize_2017(inpt[0]) + prize_2018(inpt[1])
    print(result)