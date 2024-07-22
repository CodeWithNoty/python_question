def increament(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good neeraj ")
    
a=increament(23)
print(a)