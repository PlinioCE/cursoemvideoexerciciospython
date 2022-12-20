titulo = 'Validação Função Input'
print(f'{titulo:=^40}\n')


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


numero = leia_int('Digite um número: ')
print(f'Você digitou o número {numero}.')
