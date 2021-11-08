inpt = list(map(int, input().split()))

univ_list = ['Soongsil', 'Korea', 'Hanyang']

dict = dict(zip(univ_list,inpt))

result = sorted(dict.items(), key=(lambda x:x[1]))

if sum(inpt) >= 100:
    print("OK")
else:
    print(result[0][0])
