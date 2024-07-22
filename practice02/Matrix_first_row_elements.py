list=[[1,2,3],[4,5,6],[7,8,9],[0,1,2]]
print(list)

res={list[0][ele]:list[ele+1]for ele in range(len(list)-1)}
print(res)