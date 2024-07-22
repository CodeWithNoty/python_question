com='x'
you='o'
def game(a,b,c,d,e,f,g,h,i):
     print(a,"|",b,"|",c)
     print("--|------|-----")
     print(d,"|",e,"|",f)
     print("--|------|-----")
     print(g,"|",h,"|",i)

     if com==a:
      if   you==int(input("enter  a number ")):
         return game()
print(game(1,2,3,4,5,6,7,8,9))

