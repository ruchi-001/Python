print("==== Simple Calculator ====")

while True:
    num1 = float(input("\nEnter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Cannot divide by zero.")

    else:
        print("Invalid operator!")

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for using the calculator!")
        break
