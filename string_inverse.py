def reverse(text):
    lenth = len(text)
    text_buffer = ""
    for n in range(0, lenth):
        m = lenth - n -1
        text_buffer += text[m]
    return text_buffer
