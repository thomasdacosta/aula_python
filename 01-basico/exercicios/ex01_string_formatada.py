i = 1
itens = []
qtds = []

for i in range(5):
    item = input("Digite o nome do item:")
    qtd = int(input("Digite a quantidade do item:"))

    itens.append(item)
    qtds.append(qtd)

for i in range(5):
    print(f"Item: {itens[i]} - Quantidade: {qtds[i]}")

print(itens)
print(qtds)