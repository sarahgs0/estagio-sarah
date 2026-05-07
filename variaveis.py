# Exercício 1 - Variáveis e tipos de dados
# Cria uma variável para guardar o nome
nome = "Sarah"
# Cria uma variável para guardar a idade 
idade = 16
# cria uma variável para guardar a altura
altura = 1.63
# Crie uma variável para guardar se esta chovendo
esta_chovendo = False
# Mostra o tipo da variável nome
print(type(nome))
# Mostra o tipo da variável idade
print(type(idade))
# Mostra o tipo da variável altura
print(type(altura))
# Mostra o tipo da variável esta_chovendo
print(type(esta_chovendo))

# Exercício 2 - Entrada de dados com input
# Pede para o usuário digitar o nome
nome_usuario = input("Digite seu nome: ")
# Pede para o usuário digitar a idade
idade_usuario = input("Digite sua idade: " )
# Mostra uma frase com o nome e a idade digitados
print(f"Seu nome é {nome_usuario} e você tem {idade_usuario} anos")

# Exercício 3 - Cálculo de IMC
# Pede para o usuário digitar o peso
peso = float(input("Digite seu peso: "))
# Pede para o usuário digitar a altura
altura_imc = float(input("Digite sua altura: "))
# Calcula o IMC usando peso dividido pela altura ao quadrado
imc = peso / (altura_imc * altura_imc)
# Mostra o resultado do IMC com uma casa decimal
print(f"Seu IMC é {imc:.1f}")
