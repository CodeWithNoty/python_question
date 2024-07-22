while(True):
    print("press q to quit")
    a=input("enter a numebr :")
    if a =='q':
        break
    try:
        a=int(a)
        if a>6:
            print("grater than 6")
    except Exception as e:
        print(f"error :{e}")

print("thanks ")

