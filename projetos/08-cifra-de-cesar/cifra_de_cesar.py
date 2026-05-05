import arte

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Imprimir a arte
print(arte.arte)

# Receber a entrada do usuário
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Criptografar o texto recebido
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    
    for letter in original_text:
        try:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
        except IndexError:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount - 26]
        except ValueError:
            encrypted_text += letter

    print(f"Here is the encoded result: {encrypted_text}")

# Descriptografar o texto recebido 
def decrypt(original_text, shift_amount):
    decrypted_text = ""
    
    for letter in original_text:
        try:
            decrypted_text += alphabet[alphabet.index(letter) - shift_amount]
        except IndexError:
            decrypted_text += alphabet[alphabet.index(letter) - shift_amount + 26]
        except ValueError:
            decrypted_text += letter

    print(f"Here is the decoded result: {decrypted_text}")

# Chamar a função solicitada
# if direction == "encode":
#     encrypt(original_text=text, shift_amount=shift)
# if direction == "decode":
#     decrypt(original_text=text, shift_amount=shift)

# Fundir as duas funções em uma só
restart = ""
def caesar(original_text, shift_amount, action):
    while restart != "no":
        output_text = ""
        
        if action == "encode":
            index_limit = -26
        if action == "decode":
            index_limit = 26
            shift_amount *= -1
        
        for letter in original_text:
            try:
                if letter not in alphabet:
                    output_text += letter
                else:
                    output_text += alphabet[alphabet.index(letter) + shift_amount]
            except IndexError:
                output_text += alphabet[alphabet.index(letter) + shift_amount + index_limit]
            

        print(f"Here is the {action}d result: {output_text}")
        restart = input('Type "yes" if you want to go again. Otherwise type "no".')
        
        if restart == "no":
            print("Goodbye.")

caesar(original_text=text, shift_amount=shift, action=direction)

# TODO-3: Can you figure out a way to restart the cipher program?
