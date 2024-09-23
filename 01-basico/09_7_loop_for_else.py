# ------- Descrição: Exemplos de condicionais em Python -------
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# ------- Descrição: Exemplos de condicionais em Python -------
word = "Python"
for letter in word:
    print(letter, end="*")

# ------- Descrição: Exemplos de condicionais em Python -------
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# ------- Descrição: Exemplos de condicionais em Python -------
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# ------- Descrição: Exemplos de condicionais em Python -------
text1 = "pyxpyxpyx"
for letter in text1:
    if letter == "x":
        continue
    print(letter, end="")

# ------- Descrição: Exemplos de condicionais em Python -------
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
print()

# ------- Descrição: Exemplos de condicionais em Python -------
for i in range(0, 3):
    print(i)
else:
    print(i, "else")

