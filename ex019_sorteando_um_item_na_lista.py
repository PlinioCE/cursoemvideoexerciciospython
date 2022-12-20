from random import choice

titulo = 'Escolhe Aluno'
print(f'{titulo:=^40}\n')

aluno1 = input('Digite o nome do 1º aluno(a): ')
aluno2 = input('Digite o nome do 2º aluno(a): ')
aluno3 = input('Digite o nome do 3º aluno(a): ')
aluno4 = input('Digite o nome do 4º aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('\nO escolhido foi o aluno(a) {}.'.format(choice(lista)))
