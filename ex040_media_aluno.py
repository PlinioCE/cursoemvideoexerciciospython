titulo = 'MÉDIA ALUNO'
print(f'{titulo:=^40}\n')

nome = str(input('Digite o nome do aluno(a): ')).title()
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2

if 10 >= media >= 7:
    situacao = 'APROVADO'
elif 5 <= media < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'REPROVADO'
print(f'\nALUNO(A): {nome}'
      f'\nMÉDIA: {media:.1f}'
      f'\nSITUAÇÃO: {situacao}')
