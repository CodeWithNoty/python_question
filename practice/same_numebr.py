# def test_distinct(data):
#   if len(data) == len(set(data)):
#     return False
#   else:
#     return True
# print(test_distinct([1,5,7,9]))
# print(test_distinct([2,4,5,5,7,9]))

def num(n):
    for i in n:
     if i in list[n]==list[n+1]:
        return True
     elif i in list[n]!=list[n+1]:
      print("ture")
     else:
        return False
    
print(num([1,5,7,9]))
print(num([2,4,5,5,7,9]))
