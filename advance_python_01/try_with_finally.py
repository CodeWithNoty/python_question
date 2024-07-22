try:
    i=int(input("enter  a numebr :"))
    c=1/i
except Exception as e:
    print(e)
finally:
    print("we were succesfull ")