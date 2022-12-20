titulo = 'ClassDigAlpha'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número (0 a 9999): '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('\nO número digitado foi: {}'.format(numero))
print('MILHAR: {:=2}'.format(milhar))
print('CENTENA: {}'.format(centena))
print('DEZENA: {:=2}'.format(dezena))
print('UNIDADE: {}'.format(unidade))
