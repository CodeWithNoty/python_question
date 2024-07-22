import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numebr="0123456789"
symbol="[]{},/*.-;_"

all=lower+upper+numebr+symbol
length=10

password="".join(random.sample(all,length))

print(password)