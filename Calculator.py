print("WELCOME TO CALCULATOR")
num1 = int(input("Enter the 1st number\n"))
num2 = int(input("Enter the 2nd number\n"))
print("Type the operation you wanna do +,-,*,/ ")
op = input()
if op == "+":
    print("The sum of the numbers are", num1 + num2)
elif op == "-":
    print("The diffrence of the numbers are", num1 - num2)
elif op == "*":
    print("The multiple of the numbers are".num1 * num2)
else:
    print("The division of the numbers are", num1 / num2)
