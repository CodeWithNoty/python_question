def num(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length



print(num(['php', 'exercises' ,'backend']))

