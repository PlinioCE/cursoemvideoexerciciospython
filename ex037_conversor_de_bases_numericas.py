titulo = 'CONVERSOR BASE DE DADOS'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
print('LEGENDA:'
      '\n-----------------'
      '\n[1] - BINÁRIO'
      '\n[2] - OCTAL'
      '\n[3] - HEXADECIMAL'
      '\n-----------------')
base = int(input('\nEscolha a base de conversão: '))

if base == 1:
    resultado = bin(numero)
    tipo = 'BINÁRIO'
elif base == 2:
    resultado = oct(numero)
    tipo = 'OCTAL'
elif base == 3:
    resultado = hex(numero)
    tipo = 'HEXADECIMAL'
else:
    print('OPÇÃO INVÁLIDA!')
print(f'\nO número DECIMAL {numero} convertido em {tipo} = {resultado[2:]}.')
