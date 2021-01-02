n = int(input())
n_th = n - 1

k = []
for i in range(10000000):
    j = str(i)
    if (j.count("666") > 1):
        k.append(j)

print(k[n_th])