n = int(input())

if n == 1:
    print('*')
    exit(0)

for i in range(2*n):
    for j in range(n):
        if n % 2 ==0:
            if i % 2 ==0:
                if j % 2 ==0:
                    print("*",end='')
                else:
                    if i % 2 ==0 and j == n-1:
                        print('',end='')
                    else:
                        print(' ',end='')
            else:
                if j % 2 ==0:
                    print(" ",end='')
                else:
                    print("*",end='')  

        else:
            if i % 2 ==0:
                if j % 2 ==0:
                    print("*",end='')
                else:
                    print(" ",end='')
            else:
                if j % 2 ==0:
                    if i % 2 !=0 and j == n-1:
                        print('',end='')
                    else:
                        print(' ',end='')

                else:
                    print("*",end='')        
    print()
    
