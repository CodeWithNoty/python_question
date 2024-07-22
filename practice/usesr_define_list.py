l=[]

n=int(input("enter a element "))

for i in range(0,n):
    ele=int(input())
    l.append(ele)
    print(l)

# for i in range(n):
    if l[i]-l[i-1]!=10:
     print("10 ka gap nhi hai")

    else:
        print("10 ka gap hai")