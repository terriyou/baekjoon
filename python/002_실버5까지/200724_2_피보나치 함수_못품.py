
zero_cnt = 0
one_cnt = 0

def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0:
        zero_cnt = zero_cnt + 1
        return a 
    elif n == 1: 
        one_cnt = one_cnt + 1
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

a = int(input())

for i in range(a):
    b = int(input())
    print(fibonacci(b))
    zero_cnt = 0
    one_cnt = 0