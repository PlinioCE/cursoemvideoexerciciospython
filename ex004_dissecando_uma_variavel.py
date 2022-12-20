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

a = input('Digite algo: ')
print('O tipo primitivo de {} é'.format(a),type(a))
print('1 - {} é alfanumérico?'.format(a), a.isalnum())
print('2 - {} é letra?'.format(a), a.isalpha())
print('3 - {} é número?'.format(a), a.isnumeric())
print('4 - {} é ascii?'.format(a), a.isascii())
print('5 - {} é digit?'.format(a), a.isdigit())
print('6 - {} é decimal?'.format(a), a.isdecimal())
print('7 - {} é identifier?'.format(a), a.isidentifier())
print('8 - {} é MAIÚSCULO?'.format(a), a.isupper())
print('9 - {} é minusculo?'.format(a), a.islower())
print('10 - {} é printable?'.format(a), a.isprintable())
print('11 - {} é espaço?'.format(a), a.isspace())
print('12 - {} é capitalizado?'.format(a), a.istitle())
