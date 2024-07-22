n=int(input("enter a number :"))
if n%3==0:
    print("wired")
    if n>=2 & n<=5:
        print("not wired")
    elif n>=6 & n<=20:
        print("wired")
else:
    print("not  wired")

# n = int(input("Enter an integer: "))

# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")