titulo = 'TABUADA'
print(f'{titulo:=^40}\n')

tabuada = int(input('Informe qual tabuada deseja visualizar: '))
print(f'TABUADA DE {tabuada}')
print('-' * 14)

for contagem in range(1, 11):
    resultado = tabuada * contagem
    print(f'{tabuada} x {contagem:2} = {resultado}')
