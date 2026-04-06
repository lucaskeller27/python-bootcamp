# Projeto do Dia 2 - Calculadora de gorjeta

print("### Calculadora de Gorjeta ###")

conta = float(input("Qual é o total a pagar?\n-> R$ "))
gorjeta = int(input("Qual a porcentagem de gorjeta que você gostaria de dar? (Responda somente com números)\n-> "))
pagantes = int(input("E em quantas pessoas a conta será dividida?\n-> "))

# total = (conta * ((gorjeta / 100) + 1))
total = (((gorjeta / 100) * conta) + conta)
# print(total)
racha = round((total / pagantes), 2)

# print(f"Cada pessoa deverá pagar R${racha}")
print("Cada pessoa deverá pagar R$ %.2f" %(racha))
