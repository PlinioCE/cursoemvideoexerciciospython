titulo = 'TABUADA'
print(f'{titulo:=^40}\n')

resultado = 0

while True:
    tabuada = int(input('Escolha a tabuada que deseja exibir: '))
    if tabuada < 0:
        print('\nPROGRAMA TABUADA ENCERRADO!')
        break
    print(f'\nTABUADA DE {tabuada}')
    print('-' * 15)
    for contador in range(1, 11):
        resultado = tabuada * contador
        print(f'{tabuada} x {contador:2} = {resultado}')
    print()
