# Activity: Files in Python
# Part 1 - Exercise 1 and Exercise 2
# Goal: save registrations in a file and then read those registrations


def cadastrar_pessoa():
    # Asks the user for their name
    nome = input("Enter your name: ")

    # Asks the user for their age
    idade = input("Enter your age: ")

    # Opens the cadastro.txt file in "a" mode
    # The "a" mode adds content to the end of the file without deleting what was already there
    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:

        # Writes the name and age in the file
        # The "\n" is used to start a new line
        arquivo.write(nome + " - " + idade + "\n")

    # Shows a confirmation message
    print("Registration saved successfully!")


def mostrar_cadastros():
    # Opens the cadastro.txt file in "r" mode
    # The "r" mode is used to read the file
    with open("cadastro.txt", "r", encoding="utf-8") as arquivo:

        # Shows a title before the list
        print("Saved registrations:")

        # Goes through each line in the file
        # enumerate numbers the registrations starting from 1
        for numero, linha in enumerate(arquivo, start=1):

            # Shows the registration number and the content of the line
            # strip() removes the extra line break at the end
            print(str(numero) + ". " + linha.strip())


# Down here, we choose which functions will run

# Runs the registration of one person
cadastrar_pessoa()

# Then shows all saved registrations
mostrar_cadastros()

def contar_arquivo():
    # Asks the user for the name of the file that will be analyzed
    nome_arquivo = input("Enter the file name: ")

    # Starts the line counter at zero
    linhas = 0

    # Starts the word counter at zero
    palavras = 0

    # Opens the file in "r" mode to read it
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Goes through each line in the file
        for linha in arquivo:

            # Adds 1 to the line counter
            linhas = linhas + 1

            # Splits the line into words
            palavras_da_linha = linha.split()

            # Adds the number of words in this line to the total
            palavras = palavras + len(palavras_da_linha)

    # Shows the final number of lines
    print("Number of lines:", linhas)

    # Shows the final number of words
    print("Number of words:", palavras)

 # Runs the registration of one person
# cadastrar_pessoa()

# Then shows all saved registrations
# mostrar_cadastros()

# Counts the number of lines and words in a text file
contar_arquivo()   
