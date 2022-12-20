from time import sleep

titulo = 'Função MAIOR'
print(f'{titulo:=^40}\n')


def linha():
    print('-=' * 20)


def maior(*numero):
    print('ANALIZANDO OS VALORES...')
    maiorNumero = 0
    for n in numero:
        print(f'{n}', end=' ')
        sleep(0.5)
        if n >= maiorNumero:
            maiorNumero = n
    print()
    if len(numero) == 0:
        print(f'Não foi informado número.')
        sleep(0.5)
        print('NÃO existe MAIOR número.')
        sleep(0.5)
    else:
        print(f'Foram informados {len(numero)} números.')
        sleep(0.5)
        print(f'O MAIOR número informado foi {maiorNumero}.')
        sleep(0.5)
    linha()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# Resolução Curso em Vídeo

'''from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''
