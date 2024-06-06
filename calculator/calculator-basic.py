def add(a, b):
    # Addition function
    answer = a + b
    print(str(a) + '+' + str(b) + '=' + str(answer) + "\n")

def sub(a, b):
    # Subtraction function
    answer = a - b
    print(str(a) + '-' + str(b) + '=' + str(answer) + "\n")

def mul(a, b):
    # Multiplication function
    answer = a * b
    print(str(a) + '*' + str(b) + '=' + str(answer) + "\n")

def div(a, b):
    # Division function
    answer = a / b
    print(str(a) + '/' + str(b) + '=' + str(answer) + "\n")

def main():
    while True:
        # Display menu options
        print("~~~~~~~~~~~~~~~~~~~")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")
        print("~~~~~~~~~~~~~~~~~~~")

        # Get user's choice
        choice = str(input("Give your choice: "))
        
        if choice.upper() == 'A':
            print("Addition of the two numbers. Give those two numbers now:-")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            add(a, b)

        elif choice.upper() == 'B':
            print("Subtraction of two numbers. Give those two numbers now:-")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            sub(a, b)    

        elif choice.upper() == 'C':
            print("Multiplication of two numbers. Give those two numbers now:-")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            mul(a, b)    

        elif choice.upper() == 'D':
            print("Division of two numbers. Give those two numbers now:-")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            div(a, b)    
        
        elif choice.upper() == 'E':
            # Exit the program
            print("Program Ended!")
            quit()

        else:
            print("Invalid Input!! Choose from a/b/c/d/e/A/B/C/D/E next time!!")

if __name__ == "__main__":
    main()