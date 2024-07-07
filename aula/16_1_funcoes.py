# O código abaixo é uma função que imprime a mensagem 'Olá, mundo!'
def mensagem():
    print('Olá, mundo!')


mensagem()


# O código abaixo é uma função que imprime a mensagem que é passada como argumento
def mensagem_param(msg):
    print(msg)


mensagem_param('Olá, mundo!')


# O código abaixo é uma função que imprime a mensagem que é passada como argumento
def message(number):
    print("Digite um número:", number)


number = 1234
message(1)
print(number)


# O código abaixo é uma função que imprime a mensagem que é passada como argumento
def message(what, number):
    print("Entrar", what, "número", number)


message("telefone", 11)
message("preço", 5)
message("número", "número")


def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)


introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")



