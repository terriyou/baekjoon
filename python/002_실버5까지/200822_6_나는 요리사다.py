
max = 0
max_i = 0

for i in range(5):
    sum_one = sum(list(map(int,input().split(" "))))
    if sum_one > max:
        max = sum_one
        max_i = i

print(max_i+1,max)