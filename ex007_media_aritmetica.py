titulo = str('CALCULA MÉDIA')
print(f'{titulo:=^40} \n')

aluno = input('Digite o nome do aluno(a): ')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite o 2ª nota: '))
media = (nota1 + nota2) / 2

print('\nA média do aluno(a) {} é {:.3}'.format(aluno, media))
