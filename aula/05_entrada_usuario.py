# ------- Title: Entrada do usuário -------
print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")

# ------- Title: Entrada do usuário (2) -------
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

# ------- Title: Entrada do usuário (3) -------
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# ------- Title: Entrada do usuário (4) -------
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

# ------- Title: Entrada do usuário (5) -------
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

# ------- Title: Entrada do usuário (6) -------
a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("\nIsso é tudo, pessoal!")

# ------- Title: Entrada do usuário (7) -------
name = input("Digite seu nome: ")
print("Olá, " + name + ". Prazer em conhecê-lo!")

# ------- Title: Entrada do usuário (8) -------
print("\nPressione Enter para finalizar o programa.")
input()
print("O FIM.")