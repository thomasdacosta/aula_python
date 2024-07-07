# Description: Formas de inserir elementos em listas
WHITE_PAWN = '♙'
row = []
for i in range(8):
    row.append(WHITE_PAWN)
print(row)

# Descricao: Usando list comprehension
row = [WHITE_PAWN for i in range(8)]
print(row)

# Descricao: Usando list comprehension com condicao
squares = [x ** 2 for x in range(10)]
print(squares)

# Descricao: Usando list comprehension com condicao
dds = [x for x in squares if x % 2 != 0]
print(dds)
