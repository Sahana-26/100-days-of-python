import CaeserCipher_art as CaeserCipher
import string

logo = CaeserCipher.logo
print(logo)

alpha = list(string.ascii_lowercase)
print(alpha)

special_char = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',' ']


choice = int(input('do you want to encode (type 1) or decode (type 2)\n'))
text = input('enter the text you want to encode or decode\n')
shift = int(input('enter the number of shifts\n'))
temp = list(text)
if choice == 1:
    for i in range(len(temp)):
        if temp[i] in alpha:
            temp[i] = alpha[(alpha.index(temp[i])+shift)%26]
    print('encoded code : ',''.join(temp))
elif choice == 2:
    for i in range(len(temp)):
        if temp[i] in alpha:
            temp[i] = alpha[(alpha.index(temp[i])-shift)%26]
    print('decode code : ',''.join(temp))
else:
        print('wrong choice')
