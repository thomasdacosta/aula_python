while True:
    try:
        number = int(input("Digite um número int: "))
        print(5 / number)
        break
    except ValueError:
        print("Valor errado.")
    except ZeroDivisionError:
        print("Desculpe. Não consigo dividir por zero.")
    except:
        print("eu não sei o que fazer...")

