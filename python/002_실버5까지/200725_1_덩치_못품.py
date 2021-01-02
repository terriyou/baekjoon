
iter = int(input())
dict_b = {}
list_b = []
dict_b_aft_sort = {}
b = []
for i in range(iter):
    dict_b[i] = list(map(int, input().split(' ')))

print(dict_b)     


list_b = sorted(dict_b.items(),key=lambda l:l[1], reverse=True)

for i in range(iter):
    dict_b_aft_sort[list_b[i][0]] = list_b[i][1]

print(dict_b_aft_sort)

for i in range(iter):
    tmp = list(dict_b_aft_sort.keys()).index(i)
    print(tmp + 1)