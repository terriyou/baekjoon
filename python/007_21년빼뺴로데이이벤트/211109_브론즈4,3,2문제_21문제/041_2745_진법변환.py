
dict = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15, \
    'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19, 'K' : 20, 'L' : 21, 'M' : 22, \
    'N' : 23, 'O' : 24, 'P' : 25, 'Q' : 26, 'R' : 27, 'S' : 28, 'T' : 29, \
    'U' : 30, 'V' : 31, 'W' : 32, 'X' : 33, 'Y' : 34, 'Z' : 35}

inpt_str, b = input().split()

inpt_str_rvs = inpt_str[::-1]
b = int(b)
total = 0
for i in range(len(inpt_str_rvs)):
    weight = b ** i
    try:
        int(inpt_str_rvs[i])
        if int(inpt_str_rvs[i]) >= 0 and int(inpt_str_rvs[i]) < 10:
            total += int(inpt_str_rvs[i]) * weight
    except:
        total += dict[inpt_str_rvs[i]] * weight
        
print(total)