# Projeto do Dia 5 - Gerador de senha

import random, os

os.system('cls' if os.name == 'nt' else 'clear')

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Receber entrada do usuário

print("# Bem-vindo(a) ao Gerador de Senha! #")
num_letras = int(input("Quantas letras você gostaria?\n-> "))
num_simbolos = int(input("Quantos símbolos você gostaria?\n-> "))
num_numeros = int(input("Quantos números você gostaria?\n-> "))
ordem_aleatoria = input("Você gostaria que os caracteres fiquem em ordem aleatória? (Digite S ou N)\n-> ").upper()

# Pegar a quantidade certa de cada tipo de caractere

lista_de_letras = random.choices(letras, k=(num_letras))
lista_de_simbolos = random.choices(simbolos, k=(num_simbolos))
lista_de_numeros = random.choices(numeros, k=(num_numeros))

# Adicionar todos os caracteres a uma lista

caracteres_da_senha = []
caracteres_da_senha.extend(lista_de_letras)
caracteres_da_senha.extend(lista_de_simbolos)
caracteres_da_senha.extend(lista_de_numeros)

# Verificar se o usuário deu entrada correta

if type(num_letras) != int or type(num_simbolos) != int or type(num_numeros) != int:
    print("Por favor, tente novamente digitando apenas números inteiros.")

# Embaralhar a lista e convertê-la numa cadeia

if ordem_aleatoria == "S":
    random.shuffle(caracteres_da_senha)
    random.shuffle(caracteres_da_senha)
    senha = ''.join(caracteres_da_senha)
elif ordem_aleatoria == "N":
    senha = ''.join(caracteres_da_senha)
else:
    print("Por favor, tente novamente digitando uma opção válida (S ou N).")

print(f"Sua senha personalizada é:\n-> {senha}")

# Outro método (mais longo) usando laços "for" 

# for x in range(1, (num_letras + 1)):
#     senha += random.choice(letras)

# for x in range(1, (num_simbolos + 1)):
#     senha += random.choice(simbolos)

# for x in range(1, (num_numeros + 1)):
#     senha += random.choice(numeros)