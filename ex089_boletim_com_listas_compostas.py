titulo = 'BOLETIM'
print(f'{titulo:=^40}\n')

ficha = []
contador = 0
while True:
    nome = str(input('Nome do aluno(a): ')).strip().title()
    nota1 = float(input('Nota AV1: '))
    nota2 = float(input('Nota AV2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    saida = ' '
    while saida not in 'SN':
        saida = (str(input('Deseja continuar? [S/N] ')).strip().upper()[0])
    if saida == 'N':
        break
print()
print('-=' * 13)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<8}{a[2]:>8.1f}')
print()
while True:
    detalhe = int(input('Informe o Nº do aluno(a) que deseja exibir as notas: '))
    if detalhe <= len(ficha) - 1:
        print(f'As notas de {ficha[detalhe][0]} são: {ficha[detalhe][1]}')
    else:
        print('Aluno não encontrado!')
    fechar = ' '
    while fechar not in 'SN':
        fechar = str(input('Deseja exibir as notas de outro aluno(a)? [S/N] ')).strip().upper()[0]
    if fechar == 'N':
        break
print()
print('FIM DO PROGRAMA')
