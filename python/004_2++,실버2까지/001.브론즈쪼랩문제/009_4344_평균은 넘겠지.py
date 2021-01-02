n = int(input())
for i in range(n):
    all = list(map(int, input().split()))
    num = all[0]
    del all[0]
    all_sum = sum(all)
    avg = all_sum / num
    avg_up_cnt = sum(x > avg for x in all)
    avg_up_portion = round((avg_up_cnt/num*100),3)
    print(str(format(avg_up_portion,".3f")+"%"))        
