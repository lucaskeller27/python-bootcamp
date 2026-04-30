alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'. Use the value of the user chosen 'direction' variable to determine which functionality to use. Call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

def caesar(original_text, shift_amount, action):
    output_text = ""
    
    if action == "encode":
        index_limit = -26
    if action == "decode":
        index_limit = 26
        shift_amount *= -1
    
    for letter in original_text:
        try:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
        except IndexError:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount + index_limit]
        except ValueError:
            encrypted_text += letter

    print(f"Here is the encoded result: {output_text}")

caesar(original_text=text, shift_amount=shift, action=direction)
