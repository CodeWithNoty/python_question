# def sum_even_odd(numbers):
#     even_sum = sum(num for num in numbers if num % 2 == 0)
#     odd_sum = sum(num for num in numbers if num % 2 != 0)
#     return [even_sum, odd_sum]

# # Example usage:
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = sum_even_odd(numbers_list)
# print(result)
def sum_odd_and_even(lst):
	sum_odd = 0
	sum_even = 0
	for i in lst:
		print(i)
		if i % 2:
			sum_odd += i
		else:
			sum_even += i
	return [sum_even, sum_odd]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_odd_and_even(numbers)
print(result)