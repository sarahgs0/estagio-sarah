# Activity: Error Handling in Python
# Part 2 - Try/Except
# Goal: use try/except to prevent the program from breaking when the user types something wrong

import random


def calculadora():
    # Tries to run the calculator
    try:
        # Asks the user for the first number
        number1 = float(input("Enter the first number: "))

        # Asks the user for the second number
        number2 = float(input("Enter the second number: "))

        # Asks the user for the math operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Checks if the operation is addition
        if operation == "+":
            print("Result:", number1 + number2)

        # Checks if the operation is subtraction
        elif operation == "-":
            print("Result:", number1 - number2)

        # Checks if the operation is multiplication
        elif operation == "*":
            print("Result:", number1 * number2)

        # Checks if the operation is division
        elif operation == "/":

            # Checks if the second number is not zero
            if number2 != 0:
                print("Result:", number1 / number2)

            # Shows an error message if the user tries to divide by zero
            else:
                print("Error: you cannot divide by zero.")

        # Shows a message if the operation is not valid
        else:
            print("Invalid operation.")

    # Runs this part if the user types text instead of a number
    except ValueError:
        print("Error: you need to type numbers.")


def abrir_ou_criar_arquivo():
    # Asks the user for the file name
    file_name = input("Enter the file name: ")

    # Tries to open the file in read mode
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Shows a message if the file exists
            print("File found!")

            # Reads and shows the file content
            print(file.read())

    # Runs this part if the file does not exist
    except FileNotFoundError:
        print("File not found. Creating an empty file...")

        # Creates an empty file
        with open(file_name, "w", encoding="utf-8") as file:
            pass

        # Shows a confirmation message
        print("Empty file created successfully.")


def jogo_adivinhacao():
    # Generates a random number between 1 and 20
    secret_number = random.randint(1, 20)

    # Starts the attempts counter at zero
    attempts = 0

    # Keeps the game running until the user guesses the number
    while True:

        # Tries to read the user's guess as a number
        try:
            guess = int(input("Enter your guess: "))

            # Adds 1 to the attempts counter
            attempts = attempts + 1

            # Checks if the guess is lower than the secret number
            if guess < secret_number:
                print("The secret number is higher.")

            # Checks if the guess is higher than the secret number
            elif guess > secret_number:
                print("The secret number is lower.")

            # Runs when the user guesses the secret number
            else:
                print("You got it!")
                print("Attempts:", attempts)
                break

        # Runs this part if the user types text instead of a number
        except ValueError:
            print("Error: type numbers only.")


# Menu of the program
print("1 - Calculator")
print("2 - Open or create a file")
print("3 - Guessing game")

# Asks the user to choose an option
option = input("Choose an option: ")

# Runs the calculator
if option == "1":
    calculadora()

# Runs the file opener/creator
elif option == "2":
    abrir_ou_criar_arquivo()

# Runs the guessing game
elif option == "3":
    jogo_adivinhacao()

# Shows a message if the option is invalid
else:
    print("Invalid option.")