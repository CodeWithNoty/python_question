tuple_number=[2,3,4]
print(tuple_number)
k="noty"
res=[ele for sub in tuple_number for ele in (sub,k)]
print(res)