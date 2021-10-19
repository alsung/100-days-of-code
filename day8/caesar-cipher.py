import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_amount
            final_text += alphabet[new_pos]
        else:
            final_text += char

    print(f"The {cipher_direction}d text is {final_text}")

# Print Logo
print(art.logo)


end_cipher = False

while not end_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart_loop = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart_loop == "no":
        end_cipher = True

print("Goodbye.")
