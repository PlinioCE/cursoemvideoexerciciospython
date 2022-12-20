titulo = 'FINANCIAMENTO CAITCHA'
print(f'{titulo:=^40}\n')

valorCasa = float(input('Informe o valor do financiamento: R$ '))
salario = float(input('Informe sua renda mensal: R$ '))
anos = int((input('Informe quantidade de anos do financiamento: ')))

numeroParcela = anos * 12
valorParcela = valorCasa / numeroParcela
limiteParcela = salario * 0.33

if valorParcela <= limiteParcela:
    print(f'\nO financiamento da casa no valor de R$ {valorCasa:.2f} em'
          f'{numeroParcela} parcelas iguais de R$ {valorParcela:.2f} foi APROVADO!')
else:
    print(f'\nO financiamento no valor de R${valorCasa:.2f} foi NEGADO!'
          f'Pois a parcela de R$ {valorParcela:.2f} ultrapassa 30% do salário informado(R$ {limiteParcela:.2f}).')
