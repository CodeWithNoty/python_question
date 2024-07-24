def selection_sort(data_list):
    n=len(data_list)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if data_list[j]<data_list[min_idx]:
                min_idx=j
        data_list[i],data_list[min_idx]=data_list[min_idx],data_list[i]
l=[22,34,11,56,54,2]
selection_sort(l)
print(l)