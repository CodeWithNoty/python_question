def num(l):
    for i in range(0,len(l)-1):
     for j in range(0,len(l)-1):
      if l[j]>=l[j+1]:
        swap=l[j]
        l[j]=l[j+1]
        l[j+1]=swap
    return l
print(num([8,6,7,4,5,2,3]))

# Creating a bubble sort function  
# def bubble_sort(list1):  
#     # Outer loop for traverse the entire list  
#     for i in range(0,len(list1)-1):  
#         for j in range(len(list1)-1):  
#             if(list1[j]>list1[j+1]):  
#                 temp = list1[j]  
#                 list1[j] = list1[j+1]  
#                 list1[j+1] = temp  
#     return list1  
  
# list1 = [5, 3, 8, 6, 7, 2]  
# print("The unsorted list is: ", list1)  
# # Calling the bubble sort function  
# print("The sorted list is: ", bubble_sort(list1))   