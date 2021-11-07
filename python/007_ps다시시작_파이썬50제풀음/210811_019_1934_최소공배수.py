n = int(input())

def UC(X,Y):
    while(Y):
        X,Y=Y,X%Y
    return X

def UC2(X,Y):
    result = (X*Y) // UC(X,Y)
    return result

for _ in range(n):
    inpt = list(map(int,input().split()))
    a = inpt[0]
    b = inpt[1]
    print(UC2(a,b))