n = int(input())

n_list = []

for _ in range(n):
    word = str(input())
    wlen = len(word) 
    n_list.append((wlen, word))

n_list = list(set(n_list))

n_list.sort(key = lambda word: (word[0], word[1]))

for word in n_list:
    print(word[1])