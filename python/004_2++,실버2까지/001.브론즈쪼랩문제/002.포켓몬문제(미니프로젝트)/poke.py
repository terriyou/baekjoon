f1 = open("write.txt",'w')
f2 = open("poke.txt",'r')


for i in range(1, 719):
    a = f2.readline()    
    data = f'elif n == {i}:\n'
    f1.write(data)
    poke_name = f2.readline().strip()
    data = f'  print("{poke_name}")\n'
    f1.write(data)
    poke_type = f2.readline().strip()
    data = f'  print("{poke_type}")\n'
    f1.write(data)

f1.close()
f2.close()