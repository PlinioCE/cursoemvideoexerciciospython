from time import sleep

cores_rgb = ('\033[m',          # 0 - No color
             '\033[0;30;41m',   # 1 - Red
             '\033[0;30;42m',   # 2 - Green
             '\033[0;30;43m',   # 3 - Yellow
             '\033[0;30;44m',   # 4 - Blue
             '\033[0;30;45m',   # 5 - Purple
             '\033[7m',         # 6 - Negative
             )


def cabecalho(t, cor=0):
    linha = len(t) + 4
    print(cores_rgb[cor], end='')
    print('~' * linha)
    print(t.center(linha))
    print('~' * linha)
    print(cores_rgb[0], end='')
    sleep(0.5)


def funcao(b):
    cabecalho(f'Acessando o manual do comando \'{b}\'', 4)
    print(cores_rgb[6], end='')
    sleep(1)
    help(b)
    print(cores_rgb[0], end='')


biblioteca = ' '
while True:
    cabecalho('SISTEMA DE AJUDA PyHELP', 2)
    biblioteca = str(input('Função ou Biblioteca > ')).strip().lower()
    if biblioteca == 'fim':
        break
    else:
        funcao(biblioteca)
cabecalho('ATÉ LOGO!', 1)
