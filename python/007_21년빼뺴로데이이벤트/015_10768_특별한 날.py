inpt = [int(input()) for _ in range(2)]

if inpt[0] < 2:
    print("Before")
elif inpt[0] > 2:
    print("After")
else:
    if inpt[1] < 18:
        print("Before")
    elif inpt[1] > 18:
        print("After")
    else:
        print("Special")