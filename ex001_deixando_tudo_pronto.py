# Quebra de linha - \n
# Ex: print('Configuração de \n quebra de linha')
# >>>
# Configuração de
# quebra de linha
#
# Junção de linhas - end=' '
# Ex: print('Configuração', end=' ')
#     print('de junção de linhas')
# >>>
# Configuração de junção de linhas

#Forma tradicional
print('Olá, Mundo!')
#Transformando a mensagem em variável.
msg: str = 'Olá, Mundo!'
print(msg, '\n')

nome = input('Digite seu nome: ')
print('Olá,', nome, '!')
print('Olá, {}!'.format(nome))
