
while True:
    try:
        texts = input()
    except:
        break
    if len(texts) == 0:
        break
    ord_text = 0
    ord_cnt = [0,0,0,0]
    for text in texts:
        ord_text = ord(text)
        if ord_text == 32:
            ord_cnt[3] += 1
        elif ord_text > 64 and ord_text < 91:
            ord_cnt[1] += 1
        elif ord_text > 96 and ord_text <123:
            ord_cnt[0] += 1
        elif ord_text > 47 and ord_text <58:
            ord_cnt[2] += 1
    print(ord_cnt[0],ord_cnt[1],ord_cnt[2],ord_cnt[3])
