def remove_duplicates(string):
    unique_characters = set(string)
    result = ''.join(unique_characters)
    return result

input_string = "abab"
print(remove_duplicates(input_string))  