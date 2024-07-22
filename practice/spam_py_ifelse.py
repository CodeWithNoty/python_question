Text=input("enter a text :\n")

if("make a lot of money" in Text):
    spam=True
elif("bay now" in Text):
 spam=True
elif("subscribe this "in Text):
 spam=True
elif("click this"in Text):
 spam=True
else:
 spam=False

if(spam):
 print("this text in spam")

else:
  print("this text is not spam")
  