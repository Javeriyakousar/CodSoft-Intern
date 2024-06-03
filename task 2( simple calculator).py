def add(numbers):
    return sum(numbers)

def substract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
        return result
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /=num
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

def get_numbers():
    numbers = []
    count = int(input("How many numbers do you want to use in the operation? "))
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

def calculator():
    while True:
        print("\n Select operation:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5):")
        if choice in ['1','2','3','4']:
            numbers = get_numbers()
            
            if choice == '1':
                print(f"Result: {add(numbers)}")
            elif choice == '2':
                print(f"Result: {substract(numbers)}")
            elif choice == '3':
                print(f"Result: {multiply(numbers)}")
            elif choice == '4':
                print(f"Result: {divide(numbers)}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__== "__main__":
    calculator()       
