n = int(input())

for i in range(n):
    for j in range(2*n-1):
        if i == 0 and j == (n-1):
            print("*",end='')
        elif i+j == n-1 or j-i == n-1:
            print('*',end='')
        elif j > i+n:
            print('',end='')
        else:
            print(" ",end='')
    print('')