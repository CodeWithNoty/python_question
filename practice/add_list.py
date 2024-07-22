# This function adds two numbers
def add(a,b,c,d):
    return a - b * c /d 

# This function subtracts two numbers
def subtract(a,b,c,d):
    return -a + b  /c *d

# This function multiplies two numbers
def multiply(a,b,c,d):
    return a * b - c /d

# This function divides two numbers
def divide(a,b,c,d):
    return -a / b * c + d


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
            num4 = int(input("Enter forth number: "))
    except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == '1':
            print("+",num1, "-", num2, "*" ,num3, "/", num4 ,"=",add(num1, num2, num3, num4))

    elif choice == '2':
            print("-",num1, "+", num2,"/" ,num3, "*", num4, "=", subtract(num1, num2 ,num3, num4))

    elif choice == '3':
            print("*",num1, "/", num2, "+" ,num3, "-", num4,"=", multiply(num1, num2 ,num3, num4))

    elif choice == '4':
            print("/",num1, "*", num2, "-" ,num3, "+", num4,"=", divide(num1, num2 ,num3, num4))
        
        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")