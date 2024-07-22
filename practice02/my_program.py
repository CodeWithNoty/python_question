import random
def num(n):

 if n >=11:
  return "Next Time "
    
    
 random_number = random.randint(1,10)
 print(random_number)
  
 if n==random_number:
    print("you win")
 else:
    print("you lose ?")
n=int(input("enter a number :"))
print(num(n))