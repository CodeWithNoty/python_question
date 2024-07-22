test_list = ["geeksforgeeks is best for geeks"]

print("The original list : " + str(test_list))

chr_list = ['e', 'b', 'g']

d=dict()
for i in chr_list:
	d[i]=test_list[0].count(i)
res=d
	
# printing result
print("Specific Characters Frequencies : " + str(res))
