n = int(input())
first_str = input()

for j in range(n-1):
    inpt_str = input()
    for i in range(len(first_str)):
        if inpt_str[i] != first_str[i]:
            first_str = first_str[:i] + '?' + first_str[i+1:]

print(first_str)
