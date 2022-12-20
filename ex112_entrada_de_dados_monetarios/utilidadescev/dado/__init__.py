def leia_dinheiro(texto):
    validacao = False
    while not validacao:
        entrada = str(input(texto)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! \"{entrada}\" é um valor inválido.\033[m')
        else:
            validacao = True
            return float(entrada)


def leia_int(texto):
    validacao = False
    while True:
        n = str(input(texto))
        if n.isnumeric():
            n = int(n)
            validacao = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if validacao:
            break
    return n
