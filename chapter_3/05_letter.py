letter ='''dear <|Name|
i hope you  are very happy to know that you are selected ltd compny
you are selected
have a great job 
thanku 

<|date|>
'''
print(letter)

name = input("enter your name :")
date = input("enter date :")
letter =letter.replace("<|Name|", name)
letter =letter.replace("<|date|", date)
print(letter)