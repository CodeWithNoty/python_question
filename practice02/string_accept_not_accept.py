# n=input("enter :")
# # print(str(n))
# s='!@#$%^&*()_-<>?/'
# for i in n:
#  if i in s:
#   print(f"=> {n} ")
# else:
#  print(f"{n}----your string is accepted")

def num(n):
    s=['!@#$%^&*()<>_-?/']
    for i in n:
        if i in s:
            print("not accept string")
    else:
         print("your string is accepted")
print(num('neeraj'))
print(num('neeraj@'))