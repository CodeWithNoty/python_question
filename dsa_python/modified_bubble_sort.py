def modified_bubble_sort(data_list):
    flag=False
    for r in range(1, len(data_list)):
        flag=False
        for i in range (len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
l=[22,34,11,56,54,2]
modified_bubble_sort(l)
print(l)