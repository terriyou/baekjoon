c_time = list(map(int,input().split(":")))
d_time = list(map(int,input().split(":")))

rst_time = []

c_3600time = c_time[0] * 3600 + c_time[1] * 60 + c_time[2]
d_3600time = d_time[0] * 3600 + d_time[1] * 60 + d_time[2]

if c_3600time > d_3600time:
    d_3600time += 24* 3600

rst_3600time = d_3600time - c_3600time

rst_time.append(rst_3600time // 3600)
rst_time.append((rst_3600time % 3600)//60)
rst_time.append((rst_3600time % 3600)%60)

print(f"{rst_time[0]:02d}:{rst_time[1]:02d}:{rst_time[2]:02d}")