inpt = input()

length = 10

for i in range(len(inpt)):
    try:
        if inpt[i] != inpt[i+1]:
            length = length + 10
        else:
            length = length + 5
    except:
        pass

print(length)