L = [6, 5, 4, 3, 2, 1]

for k in range(-3, 3):
    print(L[k])

# Quando chamada com um único argumento, range(n),
# ela gera uma sequência de números de 0 a n-1. Por exemplo,
# range(3) gera 0, 1, 2.
for i in range(5):
    print(i)

# Quando chamada com dois argumentos, range(start, stop),
# ela gera números começando de start até stop-1. Por
# exemplo, range(1, 4) gera 1, 2, 3.
for i in range(2, 7):
    print(i)

# Quando chamada com três argumentos, range(start, stop, step),
# ela gera números começando de start até stop-1,
# incrementando por step. Se step for negativo, a sequência é contada para trás.
# Por exemplo, range(0, -5, -1) gera 0, -1, -2, -3, -4.
for i in range(1, 11, 2):
    print(i)
