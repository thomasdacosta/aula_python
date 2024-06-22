# ------- Descrição: Exemplos de condicionais em Python -------
tax = 0
income = float(input("Entre com os rendimentos: "))

if income < 85528:
    tax = income * 0.18 - 556.02

# Escrever o resto do código aqui.
tax = round(tax, 0)
print("A taxa é:", tax, "thalers")

# ------- Descrição: Exemplos de condicionais em Python -------
year = int(input("Digite um ano: "))

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:
        print("Ano comum")
    elif year % 100 != 0:
        print("Ano bissexto")
    elif year % 400 != 0:
        print("Ano comum")
    else:
        print("Ano bissexto")