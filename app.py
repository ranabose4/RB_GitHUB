def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b if b != 0 else "Error: Division by zero"

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("Sum:", add_numbers(a, b))
    elif choice == "2":
        print("Difference:", subtract_numbers(a, b))
    elif choice == "3":
        print("Product:", multiply_numbers(a, b))
    elif choice == "4":
        print("Quotient:", divide_numbers(a, b))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()