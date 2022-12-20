titulo = 'ConverTemp'
print(f'{titulo:=^40}\n')

celsius = float(input('Temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273

print('\nConvertendo...')
print('Por favor, aguarde...')
print('\nA temperatura {:.1f}ºC, corresponde a {:.1f}ºF e a {:.1f}K.'.format(celsius, fahrenheit, kelvin))

# TABELA DE CONVERSÃO DE TEMPERATURA (ºC, ºF e K)
# K -> C >>>>>>>>>>>>> C = K - 273
# K -> F >>>>>>>>>>>>> F = ((K - 273) * 1.8) + 32
# C -> K >>>>>>>>>>>>> K = C + 273
# C -> F >>>>>>>>>>>>> F = (C * 1.8) + 32
# F -> C >>>>>>>>>>>>> C = (F - 32) / 1.8
# F -> K >>>>> K = (F - 32) * 5 / 9 + 273
