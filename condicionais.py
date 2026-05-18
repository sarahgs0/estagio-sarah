idade = input("Digite sua idade: ")
idade = int(idade)

if idade < 18:
    print("Você é menor de idade")
elif idade >= 60:
    print("Você é idoso")
else:
    print("Você é adulto")

# Exercício 2 - Conceito da nota
nota = input("Digite a nota do aluno: ")
nota = float(nota)
if nota >= 9:
    print("Conceito A")
elif nota >= 8:
    print("Conceito B")
elif nota >= 7:
    print("Conceito C")
elif nota >= 6:
    print("Conceito D")
else:
    print("Conceito F")

# Exercício 3 - Calculadora simples
# Recebe os dois números e a operação escolhida pelo usuário
numero1 = input("Digite o primeiro numero: ")
numero1 = float(numero1)
numero2 = input("Digite o segundo numero: ")
numero2 = float(numero2)
operacao = input("Digite a operação (+,-,*,/):")
# Começa sem resultado para só imprimir se a operação for válida
resultado = None
# Verifica qual operação foi escolhida e calcula o resultado
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    # Verifica se o divisor é zero antes de dividir
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = numero1 / numero2
else:
    print("Operação inválida")

# Mostra o resultado somente se a operação foi válida
if resultado is not None:
    print("Resultado:", resultado)
