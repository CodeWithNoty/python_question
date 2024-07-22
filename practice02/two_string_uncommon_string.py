def UncommonWords(A, B):

	count = {}

	for word in A.split():
		count[word] = count.get(word, 0) + 1

	for word in B.split():
		count[word] = count.get(word, 0) + 1

	return [word for word in count if count[word] == 1]


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A, B))


# Of course! Let's simplify it step by step:

# Initialization:

# The code initializes an empty dictionary called count. This dictionary will hold words encountered in both strings and their frequencies (how many times they appear).
# Counting Words:

# It then goes through each word in the first string A. It splits A into individual words using .split(), and for each word:
# If the word is already in the count dictionary, it increments its count.
# If it's not in the dictionary, it adds it with a count of 1.
# It does the same for each word in the second string B.
# Identifying Uncommon Words:

# After counting all words in both strings, it looks through the count dictionary.
# For each word in the dictionary, it checks if its count is equal to 1. If it is, it means that word only appears once in the combined strings.
# Such words are then collected into a list.
# Return:

# The function returns this list of words that are uncommon, i.e., they appear only once in the combined strings.
# Print Result:

# Finally, the code outside the function defines two strings A and B, calls the UncommonWords() function with these strings, and prints out the result.
# In summary, the function UncommonWords() calculates and returns the words that appear only once in the combination of two given strings. These words are considered "uncommon" between the two strings.





