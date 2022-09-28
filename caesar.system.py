def caesar(some_text, shift_amount, direction):
    end_text = ''
    for i in some_text:
        position = letters.index(i)
        if direction == 'encode':
           position = position + shift_amount
        elif direction == 'decode':
            position = position - shift_amount
        new_letter = letters[position]
        end_text += new_letter   
    print(end_text) 


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction_n = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
text = input("Type message: ").lower()
shift = int(input("Type the shift number: "))

caesar(some_text = text, shift_amount=shift, direction=direction_n)
