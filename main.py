
#Импортим
from caesar_vernam import CaesarCipher, VernamCipher

def run_caesar():
    print("Шифр Цезаря :")
    text = "Wo jiao Danila, ni ne"     #Китайского вам в ленту)
    shift = 11

#Шифруем
    caesar = CaesarCipher(text, shift)
    encrypted = caesar.encrypt()

    print("Исходный текст:", text)
    print("Зашифрованный текст:", encrypted)

#Расшифровываем
    decrypted = CaesarCipher(encrypted, shift).decrypt()
    print("Расшифрованный текст:", decrypted)
    print()


def run_vernam():
    print("Шифр Вернама :")
    text = "Wo shi xuesheng, wo bu shi laoshi, ni ne"     #Китайского вам в ленту)
    key = "yes"

#Шифруем
    vernam = VernamCipher(text, key)
    encrypted = vernam.encrypt()

    print("Исходный текст:", text)
    print("Ключ:", key)
    print("Зашифрованный текст:", encrypted)

#Расшифровываем
    decrypted = VernamCipher(encrypted, key).decrypt()
    print("Расшифрованный текст:", decrypted)
    print()

def main():
    run_caesar()
    run_vernam()

if __name__ == "__main__":
    main()
