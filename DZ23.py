def popular_words (text, words):
    text = str.lower(text).split(' ')
    dct = {}
    for i in words:
        dct[i] = text.count(i)
    return dct
my_text = input("Type text:")
keywords = input('Type any words to find:')
popular_words(my_text, keywords)
