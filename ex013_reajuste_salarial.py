titulo = 'CalcSalário'
print(f'{titulo:=^40}\n')

salario = float(input('Digite o valor atual do salário mensal: R$ '))
novoSalario = salario + (salario * 0.15)

print('\nCalculando...')
print('\nNovo salário com 15% de aumento: R$ {:.2f}'.format(novoSalario))
