import math
quit = 0
answer = input("""

welcome to math bot
(integers only)
type "absolute value" for absolute value"
type "factorial" for the factorial
type "squareroot" for square root
type "divide" for division
type "multiply" for multiplication
type "subtract" for subtraction
type "add" for addition
""")
while quit == 0:
    if answer == ("add"):
        num1 = int(input("enter first number you want to add:"))
        num2 = int(input("enter second number you want to add:"))
        sumplus = num1 + num2
        print(sumplus)

    elif answer == ("divide"):
        num3 = int(input("enter the number you want to be devided:"))
        num4 = int(input("enter the number you want it to be devided by:"))
        num3 /= num4
        print(num3)
    elif answer == ("multiply"):
        num5 = int(input("input your first number:"))
        num6 = int(input("input your second number:"))
        summult = num5 * num6
        print(summult)
    elif answer == ("subtract"):
        num7 = int(input("input the number you want subtracted from:"))
        num8 = int(input("input the number you to subtract from the first number:"))
        num7 -= num8
        print(num7)
    elif answer == ("squareroot"):
        num9 = int(input("input the number you want the square root of:"))
        square_root = math.sqrt(num9)
        print(square_root)
    elif answer == ("factorial"):
        num10 = int(input("input the number you want the factorial of:"))
        print(math.factorial(num10))
    elif answer == ("absolute value"):
        num11 = int(input("input the number you want the absolute value of:"))
        print(math.fabs(num11))
    elif answer == ("quit"):
        quit = 1
    else:
        print("error")
