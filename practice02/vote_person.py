def num(a):
    if a<=10:
     return "baby"
    
    elif a>=12  and a<=15:
     return "young"
    
    elif  a>=15 and a<=18:
     return "adult"
    
    elif  a>=18 and a<=20:
      return "voting"
    else :
        a>=20
        return "ajad"
print(f"{3}",num(3))
print(f"{12}",num(12))
print(f"{18}",num(18))
print(f"{20}",num(20))
print(f"{22}",num(22))