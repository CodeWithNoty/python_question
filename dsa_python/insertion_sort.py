def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while j>=0 and temp<=list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
s=[8,7,4,6,19,34,2,1]
insertion_sort(s)
print(s)
