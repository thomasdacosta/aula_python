try:
    arquivo = open("arquivos/20_1_arquivos.txt", "r")
    for linhas in arquivo.readlines():
        print(f"Linha: {linhas}")
    arquivo.close()
except Exception as erro:
    print("Erro:", erro)
finally:
    print("Fim do programa")
