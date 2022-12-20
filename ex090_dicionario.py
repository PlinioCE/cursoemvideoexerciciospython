titulo = 'SITUAÇÃO ALUNO'
print(f'{titulo:=^40}\n')

while True:
    nome = str(input('Nome: ')).strip().title()
    media = float(input(f'Média de {nome}: '))
    aluno = {'NOME': nome, 'MEDIA': media}
    print()
    print(f'Nome: {aluno["NOME"]}')
    print(f'Média: {aluno["MEDIA"]}')
    if aluno['MEDIA'] >= 7:
        aluno['SITUACAO'] = 'APROVADO'
    elif 4 <= aluno['MEDIA'] < 7:
        aluno['SITUACAO'] = 'RECUPERAÇÃO'
    else:
        aluno['SITUACAO'] = 'REPROVADO'
    print(f'Situação: {aluno["SITUACAO"]}')
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if saida == 'N':
        break
    print()
print('FIM DO PROGRAMA')

# Resolução Curso em Vídeo

'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}.')'''
