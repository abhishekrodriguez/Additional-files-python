# Faulty Calculator
# 45*3=555
# 56+9=77
# 56/6=4

Num1 = int(input("Enter the 1st number\n"))
Num2 = int(input("Enter the 2nd number\n"))
print("Enter the op +,-,*,/")
op = input()
if Num1 == 45 and Num2 == 3 and op == "*":
    print(555)
elif op == "*":
    print(Num1 * Num2)
elif Num1 == 56 and Num2 == 9 and op == "+":
    print(77)
elif op == "+":
    print(Num1 + Num2)
elif Num1 == 56 and Num2 == 6 and op == "/":
    print(4)
elif op == "/":
    print(Num1 / Num2)
else:
    print(Num1 - Num2)
