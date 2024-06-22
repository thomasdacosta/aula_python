# ------- Descrição: Exemplos de condicionais em Python -------
for i in range(10):
    print("O valor de i é atualmente", i)
print()

# ------- Descrição: Exemplos de condicionais em Python -------
# Começa no 2 e termina no 8
for i in range(2, 8):
    print("O valor de i é atualmente", i)
print()

# ------- Descrição: Exemplos de condicionais em Python -------
# Começa no 2 e termina no 8, com incremento de 3
for i in range(2, 8, 3):
    print("O valor de i é atualmente", i)
print()

# ------- Descrição: Exemplos de condicionais em Python -------
# Começa no 0 e termina no 10, com incremento de 2
for i in range(0, 10, 2):
    print("O valor de i é atualmente", i)
print()

# ------- Descrição: Exemplos de condicionais em Python -------
# Break - exemplo
print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

# ------- Descrição: Exemplos de condicionais em Python -------
# Continue - exemplo
print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

