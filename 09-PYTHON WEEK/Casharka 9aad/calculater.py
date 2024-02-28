# simple calculater in python with if statement
first_number = float(input("Please enter your first number: "))
operater = input("Choose an operater: ")
second_number = float(input("Please enter you second number: "))

if operater == "+":
    print(first_number + second_number)
elif operater == "-":
    print(first_number - second_number)
elif operater == "/":
    print(first_number / second_number)
elif operater =="*":
    print(first_number * second_number)
else:
    print("invalid operater")