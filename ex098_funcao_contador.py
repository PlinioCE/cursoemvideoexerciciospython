from time import sleep

titulo = 'Função Contagem'
print(f'{titulo:=^40}\n')


def linha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        print(f'CONTAGEM DE {inicio} a {fim} de {passo} em {passo}')
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end='  ')  # Caso o sleep não funcione, use: Ex: print(f'{c}', end='  ', flush=True)
            sleep(0.5)
        print()
        linha()
    elif inicio > fim:
        print(f'CONTAGEM DE {inicio} a {fim} de {passo} em {passo}')
        for c in range(inicio, fim - 1, -passo):
            print(f'{c}', end='  ')
            sleep(0.5)
        print()
        linha()


contador(1, 10, 1)
contador(20, 10, 2)
print('AGORA É SUA VEZ DE DEFINIR A CONTAGEM!')
numero1 = int(input('Defina o início: '))
numero2 = int(input('Defina o fim: '))
passo1 = int(input('Defina o passo: '))
contador(numero1, numero2, passo1)
