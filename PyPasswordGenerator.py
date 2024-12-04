import string
import random

alpha = list(string.ascii_letters)
print(alpha)

special_char = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
print(special_char)

digits = ['1','2','3','4','5','6','7','8','9','0']

options = ['alpha','special_char','digits']

alpha_len = int(input('how many letters would you like in your password?'))
special_char_len = int(input('how many symbols would you like?'))
digits_len = int(input('how many digits would you like?'))

dict = {'alpha':alpha_len,'special_char':special_char_len,'digits':digits_len}
dict2 = {'alpha':alpha,'special_char':special_char,'digits':digits}

password = ''

for i in range(3):
    c = random.choice(options)
    for i in range(dict[c]):     
        password+=random.choice(dict2[c])
    options.remove(c)

print(password)