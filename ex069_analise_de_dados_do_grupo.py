titulo = 'CADASTRO DE PESSOAS'
print(f'{titulo:=^40}\n')

saida = ''
totalPessoas = totalMaiores = totalHomens = totalMulheresMenos20 = 0

while saida in 'S':
    print('-------------------')
    print('CADASTRE UMA PESSOA')
    print('-------------------')
    idade = int(input('IDADE: '))
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('SEXO [M/F]: ')).upper()[0]
    totalPessoas += 1
    if idade >= 18:
        totalMaiores += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheresMenos20 += 1
    saida = ''
    while saida != 'S':
        print('-------------------------')
        saida = str(input('Deseja continar? [S/N]: ')).upper()
        if saida == 'N':
            print('\nFIM DO PROGRAMA'
                  '\n---------------')
            print(f'TOTAL: {totalPessoas} pessoas'
                  f'\nMAIORES DE 18: {totalMaiores} pessoas'
                  f'\nHOMENS: {totalHomens} pessoas'
                  f'\nMUNLHERES < 20 ANOS: {totalMulheresMenos20} pessoas')
            break
    print()

# Resolução Curso em Vídeo

'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')'''
