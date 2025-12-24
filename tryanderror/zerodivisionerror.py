# error occurred
try:
    x = int(input("Enter the number: "))
    y = int(input("Enter the number: "))
    z = x / y
    print("No error")
    print(z)

except ZeroDivisionError:
    print("Error: division by zero is not possible")

except ValueError:
    print("Error: please enter valid numbers")
  
