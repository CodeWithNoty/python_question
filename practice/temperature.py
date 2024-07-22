conversion = input("""Choose your operation.
 Choices :
 1. C to F
 2. F to C
 3. C to K
 4. K to C
 5. F to K
 6. K to F
 Q. Quit
 Your choice : """)
chiffre = float(input("Enter your temperature : "))


            
if conversion == "1":
    resultat = (f"{chiffre*(9/5)+32}°F")                   
elif conversion == "2":
    resultat = (f"{(chiffre-32)*(5/9)}°C")       
elif conversion == "3":
    resultat = (f"{chiffre+273.15}°K")        
elif conversion == "4":
    resultat = (f"{chiffre-273.15}°C")  
elif conversion == "5":
    resultat = (f"{(5/9)*(chiffre+459.67)}°K")
elif conversion == "6":
    resultat = (f"{(chiffre-273.15)*(9/5) + 32}°F")
print(f"Your result is {resultat}")