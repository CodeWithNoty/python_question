def marks(num,name):
    sum=0
    for i in num:
     sum=i+sum
     avg=sum/5
    print(name)
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print(f"Average marks of noty is ={avg}")
    if avg >= 91 and avg <= 100:
     print(f"Letter Grade of  {name} is A")

    elif avg >= 81 and avg < 91:
     print(f"Letter Grade of {name} is B")

    elif avg >= 71 and avg < 81:
     print(f"Letter Grade of {name} is C")

    elif avg >= 61 and avg < 71:
     print(f"Letter Grade of {name} is D")

    elif avg >= 51 and avg < 61:
     print(f"Letter Grade of {name} is E")

    elif avg >= 41 and avg < 51:
     print(f"Letter Grade of {name} is F")

    elif avg >= 33 and avg < 41:
     print(f"Letter Grade of {name} is E")

    elif avg >= 21 and avg < 33:
     print(f"Letter Grade of {name} is G")

    elif avg >= 0 and avg < 21:
     print(f"Letter Grade of {name} is H")

    else:
     print("Invalid Input!")
print(marks([87,54,76,67,89],"Neeraj"))
print("\n")
print(marks([43,54,56,23,43],"Noty"))

