t=[(6, 24, 12), (7, 9, 6), (12, 18, 21)]
print(str(t))
k=2
res=[i for i in t if all(ele%k==0 for ele in i)]
print(str(res))


# test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

# print("The original list is : " + str(test_list))

# K = 6

# res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]

# print("K Multiple elements tuples : " + str(res))
