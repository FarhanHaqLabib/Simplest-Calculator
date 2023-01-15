print("Necessary signs for operations:")
print("+ = Adds two number together")
print("- = Subtracts the second number from the first one")
print("* = Multiplies both number together")
print("/ = Divides the first number by the second number")


num1=input("Enter first number:")
sign=input("Enter the operation sign:")
num2=input("Input second number:")

if sign=="+":
    print(int (num1) + int (num2))

elif sign=="-":
    print(int (num1) - int (num2))

elif sign=="*":
    print(int (num1) * int (num2))

elif sign=="/":
    print(int (num1) / int (num2))

else:
    print("Syntax Error")
