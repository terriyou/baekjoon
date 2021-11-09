inpt = input()
inpt = int(inpt[:-2] + '00')
f = int(input())

for i in range(100):
    if(inpt + i) % f == 0:
        if len(str(i)) == 1:
            result = '0'+str(i)
        else:
            result = str(i)
        print(result)
        exit(0)            
