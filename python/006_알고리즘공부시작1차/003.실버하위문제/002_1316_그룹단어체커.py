n = int(input())
group_text_cnt = 0
for i in range(n):
    inpt_text = input()
    set_of_text = set(inpt_text)
    add_flag = True
    flag = True
    for idx, text in enumerate(inpt_text):
        if add_flag:
            try:
                tmp_text = text
                set_of_text.remove(text)                
                add_flag = False
            except:
                flag = False
                break
        if idx+1 < len(inpt_text) and inpt_text[idx] != inpt_text[idx+1]:
            add_flag = True
    if flag:
        group_text_cnt += 1

print(group_text_cnt)
