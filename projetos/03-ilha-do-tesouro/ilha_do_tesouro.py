# Projeto do Dia 3 - Ilha do Tesouro

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo(a) à Ilha do Tesouro.\n")
print("Sua missão é encontrar o tesouro.")

primeira_escolha = input("Você vê dois caminhos diferentes seguindo à sua frente. Você quer seguir o da esquerda (digite E) ou da direita (digite D)?\n-> ").upper()

if primeira_escolha == "D":
    print("Você se depara com uma cobra, que lhe morde e tragicamente lhe leva ao óbito. Fim de jogo.")
elif primeira_escolha == "E":
    segunda_escolha = input("Você chega a um lago com uma ilha no meio. Você tenta dar a volta pelo lago (digite L), ou nadar até a ilha (digite I)?\n-> ").upper()
    if segunda_escolha == "I":
        print("Você é atacado por um tubarão que tragicamente lhe leva ao óbito. Fim de jogo.")
    elif segunda_escolha == "L":
        terceira_escolha = input("Você encontra uns troncos de madeira e consegue fazer uma jangada para atravessar o lago. Você desembarca na ilha e encontra uma casa com três portas: uma vermelha (digite V), uma amarela (digite M), e uma azul (digite Z). Qual delas você deseja abrir?\n-> ").upper()
        if terceira_escolha == "V":
            print("Ao entrar no quarto, você cai num poço e falece tragicamente. Fim de jogo.")
        elif terceira_escolha == "Z":
            print("Você entra numa sala cheia de armadilhas e é perfurado por cem flechas. Fim de jogo.")
        elif terceira_escolha == "M":
            print("Parabéns, você encontrou o tesouro! Você venceu!")
        else:
            print("Por favor tente novamente e digite uma opção válida (V, M ou Z).")
    else: 
        print("Por favor tente novamente e digite uma opção válida (L ou I).")
else: 
    print("Por favor tente novamente e digite uma opção válida (E ou D).")
