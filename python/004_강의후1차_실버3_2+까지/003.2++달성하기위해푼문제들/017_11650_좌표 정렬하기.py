n = int(input())

n_list = []

for _ in range(n):
    n_list.append(list(map(int,input().split())))

n_list.sort(key = lambda word: (word[0], word[1]))

for word in n_list:
    print(word[0],word[1])

"""
이거 이상한데 이거 통과함
n = int(input())

n_list = []

for _ in range(n):
    inpt = input().split()
    n_list.append(list((int(inpt[0]), inpt[1])))

n_list.sort(key = lambda word: word[0])

for word in n_list:
    print(word[0],word[1])"""