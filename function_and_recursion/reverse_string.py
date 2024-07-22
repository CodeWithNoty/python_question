def string_reverse(name):

    rstr1 = ''
    index = len(name)
    while index > 0:
        rstr1 += name[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('notuy'))
