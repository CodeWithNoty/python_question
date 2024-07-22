# l=[23,45]
# count=0
# for i in (len(l)):
#     print(i)
#     if l[count]>l[count+1]:
#         True
#     else:
#         False
l = [23, 45]
count = 0
for i in range(len(l) -1):
    if l[i] > l[i + 1]:
        print(True,"greater number ")
    else:
        print(False,"not greater")