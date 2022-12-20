titulo = 'ANALISA EXPRESSÃO'
print(f'{titulo:=^40}\n')

listagem = [str(input('Digite a expressão: '))]
contadorAbre = contadorFecha = 0
for expressao in listagem:
    for parenteses in expressao:
        if parenteses in '(':
            contadorAbre += 1
        if parenteses in ')':
            contadorFecha += 1
if contadorAbre == contadorFecha:
    print(f'\nA expressão {expressao} é VÁLIDA!')
else:
    print(f'\nA expressão {expressao} é INVÁLIDA!')

# Comentário resolução Curso em Vídeo

'''exp = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')'''

# Resolução Curso em Vídeo

'''expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')'''
