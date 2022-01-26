# add
def add(a,b):
    return a+b

# subtract
def subtract(a,b):
    return a-b

# divide
def divide(a,b):
    return a/b

# multiply
def multiply(a,b):
    return a*b

# Options
print("Enter an option, this is the key.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    option = input("Enter an option: ")
    if option in("1", "2", "3", "4"):
        first_num=float(input("Enter a numbers: "))
        sec_num=float(input("Enter a second numbers: "))

        if option == "1":
            print(first_num, "+", sec_num, "=", add(first_num,sec_num))

        elif option == "2":
            print(first_num, "-", sec_num, "=", subtract(first_num,sec_num))

        elif option == "3":
            print(first_num, "x", sec_num, "=", multiply(first_num,sec_num))

        elif option == "4":
            print(first_num, "/", sec_num, "=", divide(first_num,sec_num))

    else:
        print("Enter a correct option from the key")
        break