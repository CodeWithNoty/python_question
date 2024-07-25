def Quik_sort(list):
    if len(list)<=1:
        return list
    else:
        pivot=list[0]
        lesser=[x for x  in list[1: ] if x<=pivot]
        greater=[x for x in list[1:] if x>pivot]
        return Quik_sort(lesser)+[pivot]+Quik_sort(greater)
q=[23,45,67,54,89,56]
q=Quik_sort(q)
print(q)