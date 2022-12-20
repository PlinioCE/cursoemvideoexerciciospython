titulo = str('DOBRO, TRIPLO E RAIZ QUADRADA')
print(f'{titulo:=^40} \n')

numero = int(input('Digite um número: '))
print('O dobro de {} = {}'.format(numero, numero * 2))
print('O triplo de {} = {}'.format(numero, numero * 3))
print('A raiz quadrada de {} = {:.2f}'.format(numero, numero ** 0.5))
