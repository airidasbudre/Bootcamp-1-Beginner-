code = input("Input code: ")

emoji = '⚽'
digit1 = ''
digit2 = ''

digit1 = int(code[0])
digit2 = int(code[1])
print(digit2)

digit1 = digit1 - 1
digit2 = digit2 - 1

print(digit2)

line1 = ['☐', '☐' , '☐']
line2 = ['☐', '☐' , '☐']
line3 = ['☐', '☐' , '☐']
line4 = ['☐', '☐' , '☐']
line5 = ['☐', '☐' , '☐']

map = [line1, line2, line3, line4, line5]
map[digit1][digit2] = emoji

print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")