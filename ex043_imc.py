titulo = 'IMC'
print(f'{titulo:=^40}\n')

peso = float(input('Informe seu peso(Kg): '))
altura = float(input('Informe sua altura(m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    classe = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    classe = 'PESO NORMAL'
elif 25 <= imc < 30:
    classe = 'SOBREPESO'
elif 30 <= imc < 40:
    classe = 'OBESIDADE'
else:
    classe = 'OBESIDADE MÓRBIDA'
print(f'IMC: {imc:.1f}'
      f'\nClasse: {classe}')
