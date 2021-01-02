#n = list(int(input()) for _ in range(3))
n = [int(input()) for _ in range(3)]

kake_result = str(n[0]*n[1]*n[2])

for i in range(10):
    print(kake_result.count(str(i)))