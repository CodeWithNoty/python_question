def found(n,ele):
        if ele in n:
            return "exit"
        return "not"
print(found([1,2,3,4,5],2))
print(found([1,2,3,4,5],0))
