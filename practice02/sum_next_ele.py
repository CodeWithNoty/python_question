t_sum=[(2, 4), (6, 7), (5, 1), (6, 10)]
print(str(t_sum))
res=[]
for i in range(len(t_sum)):
    for j in range(i+1,len(t_sum)):
     res.append((t_sum[i][0]+t_sum[j][0],t_sum[i][1]+t_sum[j][1]))
print(res)