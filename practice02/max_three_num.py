def main():
   a=int(input("enter a number :"))
   b=int(input("enter b number :"))
   c=int(input("enter c number :"))
   if a>b and a>c:
       print(a," is grater ")
   elif b>a and b>c:
       print(b," is greater ")
   elif c>a and c>b:
       print(c," is grater")      
if __name__=='__main__':
    main()