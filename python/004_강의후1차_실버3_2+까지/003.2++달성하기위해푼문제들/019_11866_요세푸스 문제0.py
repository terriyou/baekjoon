n,k = map(int, input().split())

n_list = [i for i in range(1,n+1)]
rst = []
idx = 0
while(n_list):
    idx += (k-1)
    if idx > len(n_list) - 1:
        idx %= len(n_list)
    rst.append(str(n_list.pop(idx)))

print("<%s>" % (', '.join(rst[i] for i in range(len(rst)))))
