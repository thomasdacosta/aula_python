try:
    value = int(input('Digite um número natural: '))
    print('O recíproco de', value, 'é', 1/value)
except ValueError:
    print('Eu não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso Universo.')