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

nome = input('Digite seu nome: ')
print('Olá,', nome, '! Seja bem-vindo(a) ao Python.')
print('Olá, {}! Seja bem-vindo(a) ao Python.'.format(nome))
print('Olá, {:20}! Seja bem-vindo(a) ao Python.'.format(nome))
print('Olá, {:>20}! Seja bem-vindo(a) ao Python.'.format(nome))
print('Olá, {:^20}! Seja bem-vindo(a) ao Python.'.format(nome))
print('Olá, {:=^20}! Seja bem-vindo(a) ao Python.'.format(nome))
print('Olá, {:*^20}! Seja bem-vindo(a) ao Python.'.format(nome))
