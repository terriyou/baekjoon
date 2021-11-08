inpt = list(map(int,input().split()))

if inpt[1] <= 2:
    print("NEWBIE!")
elif inpt[1] <= inpt[0]:
    print("OLDBIE!")
else:
    print("TLE!")