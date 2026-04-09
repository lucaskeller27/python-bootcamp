# Projeto do Dia 4 - Pedra, Papel, Tesoura

import random, os

os.system('cls' if os.name == 'nt' else 'clear')

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)______
          ________)
          _________)
         _________)
---.____________)
'''

tesoura = '''
    _______
---'   ____)______
          ________)
       ____________)
      (_____)
---.__(____)
'''

imagens_do_jogo = [pedra, papel, tesoura]

# Receber a entrada do usuário

entrada_usuario = input("Pedra, papel ou tesoura? (Digite E, A ou T)\n-> ").upper()

# Converter a entrada do usuário em inteiros, e imprimir a arte ASCII

if entrada_usuario == "E":
    escolha_usuario = 0
elif entrada_usuario == "A":
    escolha_usuario = 1
elif entrada_usuario == "T":
    escolha_usuario = 2
else:
    print("Por favor tente novamente e digite uma opção válida (E, A ou T).")
    
print(imagens_do_jogo[escolha_usuario])
    
# Receber a "escolha" do computador e imprimir a arte ASCII
    
escolha_computador = random.randint(0, 2)

print("O computador escolhe:",)
print(imagens_do_jogo[escolha_computador])

# Verificar quem ganhou e quem perdeu, e anunciar o resultado

if escolha_usuario == escolha_computador:
    print("É um empate!")
elif (escolha_usuario == 0 and escolha_computador == 1) or (escolha_usuario == 1 and escolha_computador == 2) or (escolha_usuario == 2 and escolha_computador == 0):
    print("Você perdeu.")
elif (escolha_usuario == 0 and escolha_computador == 2) or (escolha_usuario == 1 and escolha_computador == 0) or (escolha_usuario == 2 and escolha_computador == 1):
    print("Você venceu!")
else:
    print("Ocorreu um erro, por favor tente novamente.")
