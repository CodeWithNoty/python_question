def num(nums,n):

  for i in nums:
    if n == i:
     return True
  return False


print(num([1,2,3,4,5],2))
print(num([1,2,3,4,5],7))