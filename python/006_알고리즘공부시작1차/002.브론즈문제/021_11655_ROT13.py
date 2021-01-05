texts = input()
rst_texts = []

for text in texts:
    ord_text = ord(text)
    if ord_text > 64 and ord_text < 78:
        ord_text += 13
    elif ord_text > 77 and ord_text < 91:
        ord_text -= 13
    elif ord_text > 96 and ord_text < 110:
        ord_text += 13
    elif ord_text > 109 and ord_text < 123:
        ord_text -= 13
    rst_texts.append(chr(ord_text))

print("".join(rst_texts))
