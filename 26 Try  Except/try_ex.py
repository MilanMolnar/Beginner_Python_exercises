
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print("Invalid input")
    print(err)