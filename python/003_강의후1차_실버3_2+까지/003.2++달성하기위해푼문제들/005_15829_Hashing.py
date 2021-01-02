len = int(input())
inpt = input()

hash = 0

for i in range(len):
    hash += (int(ord(inpt[i]))-96) * 31 ** i

print(hash % 1234567891)