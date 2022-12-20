titulo = 'ConvertCambio'
print(f'{titulo:=^40}\n')

taxa = float(input('Digite o valor atual do dólar: R$ '))
dollar = float(input('Quantos dólares deseja comprar? '))
real = dollar * taxa

print('\nPara adquirir US$ {:.2f} você precisará desembolsar R$ {:.2f}.'.format(dollar, real))
