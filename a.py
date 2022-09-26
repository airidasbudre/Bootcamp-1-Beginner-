def encrypt(plain_text, shift_amount):
    new_text = ''
    print(plain_text)
    for i in plain_text:
        position = letters.index(i)
        i = letters[shift_amount]
        new_text += i    
    print(new_text) 


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direktion = input("Type 'encode', to encrypt, 'decode' to decrypt")

text = input("Type messege: ").lower
shift = int(input("Type the shift number"))

encrypt(plain_text = text, shift_amount = shift)

#1. string to list#