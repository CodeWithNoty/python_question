def remove_letters(string):
    return ''.join(char for char in string if not char.isalpha())

# Example usage:
original_string = "Hello123World!"
result = remove_letters(original_string)
print(result)  # Output: "123!"

 