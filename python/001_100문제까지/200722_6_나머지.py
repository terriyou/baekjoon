import collections

a = []
for i in range(10):
    a.append(int(input()) % 42) 

b = len(collections.Counter(a))
print(b)
