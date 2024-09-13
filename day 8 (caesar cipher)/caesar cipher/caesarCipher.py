import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            position = position + shift
            result += alphabet[position]
        else:
            result += char

    if direction == "encode":
        print(f"Encoded text: {result}")
    elif direction == "decode":
        print(f"Decoded text: {result}")


print(art.logo)
to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)  # calling function

    cont = input("do you want to continue? (yes or no) \n").lower()
    if cont == "no":
        print("Bye")
        to_continue = False

    # encrypt function
# def encrypt(text, shift):
#     result = ""
#     for char in text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             position = (position + shift )% 26
#             result += alphabet[position]
#     print(f"The encoded text is {result}")


# decrypt function
# def decrypt(cipher_text,shift_amount):
#     result=""
#     for char in text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             position = (position - shift )% 26
#             result += alphabet[position]
#     print(f"The decoded text is {result}")

# decision
# if direction == "encode":
#     encrypt(text,shift) # parameters arguements
# elif direction == "decode":
#     decrypt(cipher_text= text,shift_amount = shift) #keyword arguements
