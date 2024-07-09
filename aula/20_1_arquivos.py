try:
    arquivo = open("arquivos/20_1_arquivos.txt", "w")
    for i in range(1000):
        arquivo.write(f"Olá, mundo na posição {i}\n")
    arquivo.close()
except Exception as erro:
    print("Erro:", erro)
finally:
    print("Fim do programa")

