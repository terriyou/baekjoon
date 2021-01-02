def fact(n): 
    if n==0:        
        return 1
    return n * fact(n-1)
inpt = int(input())
print(fact(inpt))