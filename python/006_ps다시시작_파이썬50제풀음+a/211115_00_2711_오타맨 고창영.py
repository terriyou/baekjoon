n = int(input())

for i in range(n):
    idx, inpt_str = input().split()
    idx = int(idx)
    result = inpt_str[:idx-1] + inpt_str[idx:]
    print(result)
