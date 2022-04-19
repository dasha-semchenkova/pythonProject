import random, time
from math import log, ceil

print('Добро пожаловать в числовую угадайку!')
def is_valid1(num):
    while True:
        if num.isdigit() and int(num) >= 10:
            return True
        else:
            return False

while True:
    limit_val = input('Введи любое число, которое ты хочешь сделать граничным значением для числовой угадайки (оно должно быть больше 10): ')
    time.sleep(1.3)
    if not is_valid1(limit_val):
        print(f'А может быть все-таки введешь целое число, которое больше 10?')
        time.sleep(1.3)
        continue
    else:
        break
limit_val = int(limit_val)
time.sleep(1.3)

rnd_num = random.randint(1, limit_val)

def is_valid2(num):
    while True:
        if num.isdigit() and 1 <= int(num) <= limit_val:
            return True
        else:
            return False

def guess_number():
    count = ceil(log(limit_val, 2) + 2)
    print(f'Тебе нужно угадать число, которое лежит в диапазоне от 1 до {limit_val}. У тебя всего {count} попыток!')
    time.sleep(1.3)

    while True:
        gss_num = input(f'Введи число от 1 до {limit_val}: ')
        time.sleep(1.3)
        if not is_valid2(gss_num):
            print(f'А может быть все-таки введешь целое число от 1 до {limit_val}?')
            time.sleep(1.3)
            continue
        gss_num = int(gss_num)

        if rnd_num < gss_num:
            count -= 1
            print(f'Твоё число больше загаданного, попробуй еще разок. У тебя осталось {count} попыток.')
            time.sleep(1.3)
        elif rnd_num > gss_num:
            count -= 1
            print(f'Твоё число меньше загаданного, попробуй еще разок. У тебя осталось {count} попыток.')
            time.sleep(1.3)
        elif rnd_num == gss_num:
            count -= 1
            print(f'Ты угадал, поздравляю! А у тебя осталось еще {count} попыток!')
            break
        if count == 0:
            return (f'Сорри, но все попытки исчерпаны :( Кстати, я загадал число {rnd_num}.')
            time.sleep(1.3)


def play_question():
    question = input('Не хочешь сыграть ещё раз? Введи Да или Нет: ')
    if question in ['ДА', 'да', 'Да', 'дА', 'LF', 'lf', 'Lf', 'lF']:
        print(guess_number())
    else:
        print('Спасибо, что сыграл в числовую угадайку! Ещё увидимся...')


print(guess_number())
print(play_question())

