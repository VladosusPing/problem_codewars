def pig_it(text):
    text = text.split(" ")
    ret = ""
    for i in range(len(text)):
        if text[i].isalpha() == True:
            for j in range(1, len(text[i])):
                ret += (text[i][j])
            ret += (text[i][0])
            ret += ("ay ")
        else:
            ret += text[i]

    return ret
