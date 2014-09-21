def censor(text, word):
    lenth = len(word)
    asterisks = '*' * lenth
    items = text.replace(word, asterisks)
    return items
print censor("this hack is wack hack", "hack")
