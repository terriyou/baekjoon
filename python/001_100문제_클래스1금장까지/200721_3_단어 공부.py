import collections

def check_freq(str):
    freq = collections.Counter(str)
    for i in range (97,123):
        if chr(i) in freq:
            if not chr(i-32) in freq:
                freq[chr(i-32)] = freq[chr(i)]
                del freq[chr(i)]
            else:
                freq[chr(i-32)] = freq[chr(i-32)] + freq[chr(i)]
                del freq[chr(i)]
    return freq

a = input()
b = check_freq(a)    
c = sorted(b.items(),key=lambda x: x[1],reverse=True)
if len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] == c[1][1]:
        print("?")
    else:
        print(c[0][0])