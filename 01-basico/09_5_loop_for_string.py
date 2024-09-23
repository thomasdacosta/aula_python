var = input("Digite uma frase:")
word_without_vowels = ""

for letra in var:
    if letra == "A" or letra == "a":
        continue
    elif letra == "e" or letra == "E":
        continue
    elif letra == "i" or letra == "I":
        continue
    elif letra == "o" or letra == "O":
        continue
    elif letra == "u" or letra == "U":
        continue
    word_without_vowels += letra.upper()

print(word_without_vowels)