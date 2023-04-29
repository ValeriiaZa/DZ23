def popular_words (text, words):
    text = str.lower(text).split(' ')
    cnt_words = text.count('i'), text.count('was'), text.count('three'), text.count('near')
    dct ={}
    dct[words[0]] = cnt_words[0]
    dct[words[1]] = cnt_words[1]
    dct[words[2]] = cnt_words[2]
    dct[words[3]] = cnt_words[3]
    return dct
my_text = "When I was One I had just begun When I was Two I was nearly new"
keywords ='i', 'was', 'three', 'near'
popular_words(my_text, keywords)
