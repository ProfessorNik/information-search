from functools import reduce


def caesar_cipher(input_file, output_file, shift, language):
    if language == 'english':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif language == 'russian':
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        print("Неподдерживаемый язык")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    encrypted_text = reduce(
        lambda encryption_text, cur_char: encryption_text + encrypt_symbol(cur_char, shift, alphabet),
        text,
        ''
    )

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    print("Текст зашифрован и сохранен в файле", output_file)


def encrypt_symbol(char, shift, alphabet):
    if char.lower() in alphabet:
        index = (alphabet.index(char.lower()) + shift) % len(alphabet)
        if char.isupper():
            return alphabet[index].upper()
        else:
            return alphabet[index]
    else:
        return char


def open_files_and_encrypt():
    input_file = input("Введите путь до изначального файла с текстом: ")
    output_file = input("Введите путь до файла, куда сохранить зашифрованный текст: ")
    shift = int(input("Введите требуемый сдвиг: "))
    language = input("Выберите язык текста (английский или русский): ")
    caesar_cipher(input_file, output_file, shift, language)


open_files_and_encrypt()
