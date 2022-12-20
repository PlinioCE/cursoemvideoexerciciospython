titulo = 'CalcDesconto'
print(f'{titulo:=^40}\n')

valor = float(input('Qual o valor da compra? R$ '))
desconto = int(input('Qual o valor do desconto? (%): '))
total = valor - (valor * desconto / 100)

print('')
print('-' * 20)
print('Valor: R$ {:>7.2f}'.format(valor))
print('DESCONTOS: {:5}%'.format(desconto))
print('TOTAL: R$ {:>7.2f}'.format(total))
print('-' * 20)
print('\nOBRIGADO E VOLTE SEMPRE.')
