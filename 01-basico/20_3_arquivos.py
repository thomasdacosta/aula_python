with open("arquivos/20_3_arquivos.txt", 'w') as file:
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)
