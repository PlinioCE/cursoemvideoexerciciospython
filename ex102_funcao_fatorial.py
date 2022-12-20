titulo = 'Fatorial True'
print(f'{titulo:=^40}\n')


def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: O número a ser calculado o fatorial;
    :param show: (Opcional) caso o usuário deseje exibir o cálculo;
    :return: O valor do fatorial do número.
    """
    f = 1
    print(f'{numero}! = ', end='')
    for n in range(numero, 0, -1):
        f *= n
        if show:
            if n == 1:
                print(f'{n} = ', end='')
            else:
                print(f'{n} x ', end='')
    return f


num = int(input('Digite um número: '))
exibir = str(input('Deseja exibir o cálculo? [S/N]: ')).strip().upper()[0]
while exibir not in 'SN':
    exibir = str(input('Deseja exibir o cálculo? [S/N]: ')).strip().upper()[0]
if exibir == 'S':
    exibir = True
else:
    exibir = False
print()
print(fatorial(num, exibir))
print()
help(fatorial)


# Resolução Curso em Vídeo

'''def fatorial1(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(fatorial1(5, show=True))
help(fatorial)'''
