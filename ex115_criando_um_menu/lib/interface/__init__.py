cores_ansi = ('\033[m',          # 0 - No color
              '\033[0;30;41m',   # 1 - Red
              '\033[0;30;42m',   # 2 - Green
              '\033[0;30;43m',   # 3 - Yellow
              '\033[0;30;44m',   # 4 - Blue
              '\033[0;30;45m',   # 5 - Purple
              '\033[7m',         # 6 - Negative
              )


def leia_int(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[34mO usuário decidiu não informar o valor inteiro\033[m.')
            return 0
        except Exception as erro:
            print(f'\033[31mERRO: {erro.__class__} / {erro.__cause__}')
        else:
            return n


def linha():
    return '-' * 40


def cabecalho(texto):
    print(linha())
    print(texto.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leia_int('\033[33mInforme a opção:\033[m ')
    return opcao