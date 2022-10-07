def is_valid_num(num):
    while True:
        if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
            return int(num)
        else:
            num = input('Ввести можно только одно положительное или отрицательное число: ')


def ceaser_cipher():
    language = input('Какой язык выберешь: английский/русский? ').lower()
    while language.startswith('англ') != True and language.startswith('рус') != True:
        language = input('Введи корректное значение! Английский/русский? ').lower()

    step = input('Напиши шаг сдвига: ')
    is_valid_num(step)

    text = input('Введи текст, который хочешь зашифровать: ')
    if 'ё' in text:
        text.replace('ё', 'е')
    elif 'Ё' in text:
        text.replace('Ё', 'Е')
    while text.isalpha() == False and text.isspace():
        text = input('Внимательней! Введи текст, который хочешь зашифровать: ')

    if language.startswith('англ'):
        alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        mod = 26
    else:
        alf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
        mod = 32
    cipher = ''
    for i in text:
        if i.isupper():
            cipher += alf[(alf.find(i) + int(step)) % mod]
        elif i.islower():
            cipher += alf[(alf.find(i) + int(step)) % mod + mod]
        else:
            cipher += i
    return cipher

def play_question():
    question = input('Хочешь попробовать ещё раз? Введи Да или Нет: ')
    while question in ['ДА', 'да', 'Да', 'дА', 'LF', 'lf', 'Lf', 'lF']:
        print(ceaser_cipher())
        print(play_question())
    else:
        return 'Спасибо, что заглянул! Ещё увидимся...'


print(ceaser_cipher())
print(play_question())

# буква ё, язык проверить, символы - спасибо, что написала
