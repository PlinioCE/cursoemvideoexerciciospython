titulo = 'Calc Reajuste Salarial'
print(f'{titulo:=^40}\n')

salarioAtual = float(input('Digite o salário mensal atual: R$ '))

if salarioAtual >= 1250:
    salarioNovo = salarioAtual + (salarioAtual * 0.1)
else:
    salarioNovo = salarioAtual + (salarioAtual * 0.15)
print('\nNOVO SALÁRIO: R$ {:.2f}'.format(salarioNovo))
