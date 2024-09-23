hat_list = [1, 2, 3, 4, 5]  # Esta é uma lista atual de números ocultos no hat.

valor = int(input("Digite um valor que substitua o número do meio por um número inteiro: "))
hat_list[2] = valor
print(hat_list)

del hat_list[-1]

print(len(hat_list))
print(hat_list)
