n= "Hello, World!"
print(type(n))

# Input string
input_string = "neeraj"

# Initialize an empty string for the reversed version
reversed_string = ""

# Iterate through the input string in reverse order and build the reversed string
for i in range(len(input_string) - 1, -1, -1):
    reversed_string += input_string[i]

# Print the reversed string
print(reversed_string)
