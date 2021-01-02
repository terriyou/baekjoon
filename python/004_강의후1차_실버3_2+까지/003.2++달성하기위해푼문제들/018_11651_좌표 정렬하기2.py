n = int(input())

n_list = []

for _ in range(n):
    n_list.append(list(map(int,input().split())))

n_list.sort(key = lambda word: (word[1], word[0]))

for word in n_list:
    print(word[0],word[1])