a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

def split_start_n_end(inpt):
    result = []
    strt = []
    ed = []
    for i in range(3):
        strt.append(inpt[i])
    for i in range(3,6):
        ed.append(inpt[i])
    result.append(strt)
    result.append(ed)
    return result

def calc_to_sec(inpt):
    outpt = inpt[0] * 3600 + inpt[1] * 60 + inpt[2]
    return outpt

def calc_end_minus_start(inpt):
    result = []
    total_sec = inpt[1] - inpt[0]
    rst_hour = total_sec // 3600
    rst_min = (total_sec % 3600) // 60
    rst_sec = total_sec % 60
    result.append(str(rst_hour))
    result.append(str(rst_min))
    result.append(str(rst_sec))
    return result

def calc_result(a):
    a = split_start_n_end(a)
    a_start_sec = calc_to_sec(a[0])
    a_end_sec = calc_to_sec(a[1])
    tmp =  []
    tmp.append(a_start_sec)
    tmp.append(a_end_sec)
    print(' '.join(calc_end_minus_start(tmp)))

calc_result(a)
calc_result(b)
calc_result(c)