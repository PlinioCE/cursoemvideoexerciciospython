from random import randint
from time import sleep

titulo = 'Função Sorteio'
print(f'{titulo:=^40}\n')


def sorteio(lista):
    print('Sorteando 5 números... ', end='')
    for contagem in range(0, 5):
        n = randint(0, 9)
        print(n, end=' ')
        sleep(0.5)
        lista.append(n)
    print()


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores PARES de {lista}, temos {soma}.')


listaNumeros = list()
sorteio(listaNumeros)
soma_par(listaNumeros)
