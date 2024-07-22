n = 'geeksforgeeks'

print("The original string is : " + str(n))

a = len(n) // 2

l = ''
for i in range(len(n)):

	if i >= a:
		l +=n[i].upper()
	else:
		l += n[i]

print("The resultant string : " + str(l))