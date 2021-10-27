import random
import symbols


def requirements():
    chars = []

    amount = int(input('Введите количество генерируемых паролей: '))
    length = int(input('Введите длину пароля: '))

    num = input('Пароль должен содержать цифры? да/нет ').lower()
    if num == 'да':
        chars.extend(symbols.digits)

    up = input('Пароль должен содержать прописные буквы? да/нет ').lower()
    if up == 'да':
        chars.extend(symbols.uppercase)

    low = input('Пароль должен содержать строчные буквы? да/нет ').lower()
    if low == 'да':
        chars.extend(symbols.lowercase)

    punk = input('Пароль должен содержать знаки пунктуации? да/нет ').lower()
    if punk == 'да':
        chars.extend(symbols.punct)

    spor = input('Пароль может содержать спорные символы? да/нет ').lower()
    if spor != 'нет':
        for ch in 'il1Lo0O':
            if ch in chars:
                chars.remove(ch)

    return chars, amount, length


def generate_password(chars, amount, length):
    passwords = []
    for _ in range(amount):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        passwords.append(password)
    return passwords


def save_passwords(passwords):
    with open('passwords.txt', 'a') as file:
        for password in passwords:
            print(f'Сгенерирован пароль {password}')
            file.write(f'{password}\n')
        file.close()


req = requirements()
passwords = generate_password(*req)
save_passwords(passwords)
