# Descrição: Criação de uma matriz 31x24 com valores 0
temps = [[0.0 for h in range(24)] for d in range(31)]
for day in temps:
    print(day)

# Descrição: Cálculo da temperatura média ao meio-dia
temps = [[0.0 for h in range(24)] for d in range(31)]
total = 0.0

for day in temps:
    total += day[11]

average = total / 31
print("Temperatura média ao meio-dia:", average)
