import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

amount = int(input('Укажите количество паролей для генерации: '))
length = int(input('Укажите длину одного пароля: '))
digit = (input('Включать ли цифры - 0123456789? д-да/н-нет: '))
up_letter = (input('Включать ли прописные буквы - ABCDEFGHIJKLMNOPQRSTUVWXYZ? д-да/н-нет: '))
low_letter = (input('Включать ли строчные буквы - abcdefghijklmnopqrstuvwxyz? д-да/н-нет: '))
punct = (input('Включать ли символы - !#$%&*+-=?@^_? д-да/н-нет: '))
str_symb = (input('Исключать ли неоднозначные символы - il1LIo0O? д-да/н-нет: '))

if digit.lower() == 'д':
    chars += digits
if up_letter.lower() == 'д':
    chars += uppercase_letters
if low_letter.lower() == 'д':
    chars += lowercase_letters
if punct.lower() == 'д':
    chars += punctuation
if str_symb.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password():
    for i in range(int(amount)):
        print(*random.sample(chars, length), sep='')


print(generate_password())

        
