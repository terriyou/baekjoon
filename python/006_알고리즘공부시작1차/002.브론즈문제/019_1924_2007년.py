x,y = map(int,input().split())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

rst = sum(month[0:x]) + y

if rst % 7 == 1:
    print("MON")
elif rst % 7 == 2:
    print("TUE")
elif rst % 7 == 3:
    print("WED")
elif rst % 7 == 4:
    print("THU")
elif rst % 7 == 5:
    print("FRI")
elif rst % 7 == 6:
    print("SAT")
elif rst % 7 == 0:
    print("SUN")
