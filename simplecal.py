num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
op = input("Enter the operation you want to perform")
match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)

 