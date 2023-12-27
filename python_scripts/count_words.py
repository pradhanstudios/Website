def word_count(s):
    temp = {}

    s = s.split()

    for word in s:
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1

    return temp