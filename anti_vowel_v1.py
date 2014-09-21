def anti_vowel(text):
    items = ['a', 'A', 'E', 'e', 'i', 'I', 'o', 'O', 'u', 'U']
    for item in items:
        if item in text:
            text = text.replace(item,'')
    return text    
