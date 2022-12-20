titulo = 'SEQUÊNCIA DE FIBONACCI'
print(f'{titulo:=^40}\n')

numero = int(input('Digite a quantidade de números que deseja exibir: '))

contagem = 3
termo0 = 0
termo1 = 1
print(f'\n{termo0} >>> {termo1} >>> ', end='')

while contagem <= numero:
    contagem += 1
    proximoTermo = termo0 + termo1
    termo0 = termo1
    termo1 = proximoTermo
    print(f'{proximoTermo} >>>', end=' ')
print('FIM')

