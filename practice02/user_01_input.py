def Number(user):
    for user in range(0,20):
        if user % 2== 0:
            return "Even"
        else:
         return "Odd"
    pass
user=input("Enter ")
print(Number(user))