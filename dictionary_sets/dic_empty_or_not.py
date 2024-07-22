from  collections import Counter
dic1={'a':30,'b':20}
dic2={'a':30,'b':20}

d=Counter(dic1) + Counter(dic2)
print(d)