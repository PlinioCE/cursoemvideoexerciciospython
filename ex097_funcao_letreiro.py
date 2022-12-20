titulo = ' LETREIRO '
print(f'{titulo:=^40}\n')


def escreva(texto):
    linha = len(texto) + 4
    print('~' * linha)
    print(texto.center(linha))  # print(f'  {texto}')
    print('~' * linha)


saudacao = str(input('Qual mensagem deseja exibir? ')).strip()
escreva(saudacao)
