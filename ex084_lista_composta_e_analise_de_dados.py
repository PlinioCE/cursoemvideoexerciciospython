titulo = 'CADASTRO PESO'
print(f'{titulo:=^40}\n')

pessoa = list()
grupoPessoas = list()
pessoaLeve = list()
pessoaPesada = list()
menorPeso = maiorPeso = 0
while True:
    pessoa.append(str(input('Digite o nome: ')).strip().title())
    pessoa.append(int(input('Digite o peso: ')))
    if len(grupoPessoas) == 0:
        menorPeso = maiorPeso = pessoa[1]
    else:
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
        elif pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
    grupoPessoas.append(pessoa[:])
    pessoa.clear()
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print()
    if saida == 'N':
        break
for p in grupoPessoas:
    if p[1] == menorPeso:
        pessoaLeve.append(p[0])
    elif p[1] == maiorPeso:
        pessoaPesada.append(p[0])
print(f'Foram cadastradas {len(grupoPessoas)} pessoas.')
print(f'O MAIOR peso foi {maiorPeso}Kg, encontrado em {pessoaPesada}')
print(f'O MENOR peso foi {menorPeso}Kg, encontrado em {pessoaLeve}')
