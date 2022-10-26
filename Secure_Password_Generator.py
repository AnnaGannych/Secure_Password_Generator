import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
chars_1 = ''


def is_digit():
    while True:
        x = input()
        if x.isdigit():
            return int(x)
        else:
            print('Введите число')
            continue


print('Введите количество паролей для генерации')
passwords = is_digit()

print('Введите длину одного пароля')
length = is_digit()


def yes_no():
    while True:
        print('ДА / НЕТ')
        y = input().lower()
        if y == 'да':
            return True
        if y == 'нет':
            return False
        else:
            print(y)
            print('Не понял. Повторите.')
            continue


print('Пароль должен включать цифры 0123456789 ?')
numbers = yes_no()
if numbers == True:
    chars += digits

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?')
capital_letters = yes_no()
if capital_letters == True:
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?')
lower_case = yes_no()
if lower_case == True:
    chars += lowercase_letters

print('Включать ли символы !#$%&*+-=?@^_ ?')
symbols = yes_no()
if symbols == True:
    chars += punctuation

print('Исключать ли неоднозначные символы il1Lo0O ?')
ambiguous_characters = yes_no()
if ambiguous_characters == True:
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            chars_1 += chars[i]
        else:
            continue
if ambiguous_characters == False:
    chars_1 = chars


def generate_password(length, chars_1):
    password = ''
    for _ in range(length):
        password += random.choice(chars_1)
    return password

print('Cгенерированные пароли:')
for _ in range(passwords):
    print(generate_password(length, chars_1))
print('Генерация паролей закончена.')
