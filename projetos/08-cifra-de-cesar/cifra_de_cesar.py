alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    
    for letter in original_text:
        try:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
        except IndexError:
            encrypted_text += alphabet[alphabet.index(letter) + (shift_amount) - 26]
        except ValueError:
            encrypted_text += letter

    print(f"Here is the encoded result: {encrypted_text}")

def decrypt(encrypted_text, shift_amount):
    pass

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
if direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift)
