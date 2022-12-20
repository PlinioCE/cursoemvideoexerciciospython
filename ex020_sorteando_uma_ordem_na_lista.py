from random import shuffle

titulo = 'Ordem de Apresentação'
print(f'{titulo:=^40}\n')

aluno1 = input('Digite o nome do 1º aluno(a): ')
aluno2 = input('Digite o nome do 2º aluno(a): ')
aluno3 = input('Digite o nome do 3º aluno(a): ')
aluno4 = input('Digite o nome do 4º aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem de apresentação será:', lista)
#print('A ordem será:\n1º aluno(a): {}\n2º aluno(a): {}\n3º aluno(a): {}\n4º aluno(a): {}')