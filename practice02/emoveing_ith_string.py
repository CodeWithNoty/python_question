def num(string , n):
    if n<0 and  n>=len(string):
        return "invaild syntax"
    return string[:n] + string[n+1:]
in_string="noutiyal"
n=5
result=num(in_string,n)
print(result)

# def remove_ith_character(string, i):
#     if i < 0 or i >= len(string):
#         return "Invalid index"
#     return string[:i] + string[i+1:]

# # Example usage:
# input_string = "example"
# i = 2
# result = remove_ith_character(input_string, i)
# print("Result:", result)
