inpt = int(input())

rest = 1000 - inpt

rest_list = []

rest_list.append(rest // 500)
rest_list.append((rest % 500) // 100)
rest_list.append((rest % 100) // 50)
rest_list.append((rest % 50) // 10)
rest_list.append((rest % 10) // 5)
rest_list.append((rest % 5) // 1)

print(sum(rest_list))

