inpt = list(map(int,input().split()))
inpt.sort()
print(abs(inpt[0]+inpt[3] - (inpt[1] + inpt[2])))