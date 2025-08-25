#CALCULATOR
#Design a simple calculator with basic arithmetic operations.Perform the calculation and display the result.


print("\t---CALCULATOR---")

num1=float(input("Enter first number = "))
choice=input("Enter operation choice (+,-,*,/) = ")
num2=float(input("Enter second number = "))

if (choice == "+"):
    print(f"Result={num1+num2}")

elif(choice == "-"):
    print(f"Result={num1-num2}")

elif(choice == "*"):
    print(f"Result={num1*num2}")

elif(choice == "/"):
    print(f"Result={num1/num2}")

else:
    print("Please enter valid opeartion")