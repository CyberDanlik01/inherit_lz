#Импортим
from caesar_vernam import CaesarCipher, VernamCipher

print("Шифр Цезаря :")
text_1 = "Wo jiao Danila, ni ne"      #Китайского вам в ленту)
shift = 11

#Шифровка
caesar = CaesarCipher(text_1, shift)
encrypted_c = caesar.encrypt()
print("Исходный текст :", text_1)
print("Зашифрованный текст :", encrypted_c)

#Расшифровка
caesar2 = CaesarCipher(encrypted_c, shift)
print("Расшифрованный текст :", caesar2.decrypt())

print("Шифр Вернама :")
text_2 = "Wo shi xuesheng, wo bu shi laoshi, ni ne"    #Китайского вам в ленту)
key = "yes"

#Шифровка
vernam = VernamCipher(text_2, key)
encrypted_v = vernam.encrypt()
print("Исходный текст :", text_2)
print("Ключ :", key)
print("Зашифрованный текст :", encrypted_v)

#Расшифровка
vernam2 = VernamCipher(encrypted_v, key)
print("Расшифрованный текст:", vernam2.decrypt())