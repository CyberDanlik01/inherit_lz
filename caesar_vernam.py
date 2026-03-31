
#Вариант - 9(шифр)

#МЕТОД ЦЕЗАРЯ
class CaesarCipher:
    def __init__(self, input_text, shift):
        self.input_text = input_text
        self.shift = shift
#Шифровка
    def encrypt(self):
        result = ""
        for char in self.input_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + self.shift) % 26 + base)
                result += new_char
            else:
                result += char
        return result
#Расшифровка
    def decrypt(self):
        result = ""
        for char in self.input_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base - self.shift) % 26 + base)
                result += new_char
            else:
                result += char
        return result

#МЕТОД ВЕРНАМА
class VernamCipher(CaesarCipher):
    def __init__(self, input_text, key_word):
        super().__init__(input_text, 0)
        self.key_word = key_word
#Шифровка
    def encrypt(self):
        result = ""
        key = self.key_word
        for i in range(len(self.input_text)):
            char = self.input_text[i]
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[i % len(key)]
                key_shift = ord(key_char.lower()) - ord('a')
                new_char = chr((ord(char) - base + key_shift) % 26 + base)
                result += new_char
            else:
                result += char
        return result
#Расшифровка
    def decrypt(self):
        result = ""
        key = self.key_word
        for i in range(len(self.input_text)):
            char = self.input_text[i]
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key[i % len(key)]
                key_shift = ord(key_char.lower()) - ord('a')
                new_char = chr((ord(char) - base - key_shift) % 26 + base)
                result += new_char
            else:
                result += char
        return result