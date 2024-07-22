import random

def gamewin(comp,you):
    if comp==you:
        return None
  #when computter all posiilities r  
    elif comp=='r':
        if you=='p':
            return False
        if you=='s':
            return True

#when computter all posiilities p 
    elif comp=='p':
        if you=='s':
            return False
        if you=='r':
            return True
        
#when computter all posiilities s 
    elif comp=='s':
        if you=='r':
            return False
        if you=='p':
            return True
        
#computer choice        
print("comp turn : rock(r) paper(p) sizer(s)")
randomno=random.randint(1,3)

if randomno==1:
    comp='r'

if randomno==2:
    comp='p'

if randomno==3:
    comp='s'

#your choice
you=input("your turn : rock(r) paper(p) sizer(s)")
a=gamewin(comp,you)

print(f"computer choice {comp}")
print(f"your  choice {you}")

if a==None:
 print("the gamae is tie")

elif a:
    print("you win ")

else:
    print("the game is over")