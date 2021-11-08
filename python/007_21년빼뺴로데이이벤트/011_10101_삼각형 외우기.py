inpt = [int(input()) for _ in range(3)]

if sum(inpt) != 180:
    print("Error")
elif inpt[0] == 60 and inpt[1] == 60:
    print("Equilateral")
elif inpt[0] == inpt[1] or inpt[1] == inpt[2] or inpt[0] == inpt[2]:
    print("Isosceles")
else:
    print("Scalene")