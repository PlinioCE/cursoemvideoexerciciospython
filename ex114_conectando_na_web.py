import urllib
import urllib.request

titulo = 'SITE PUDIM'
print(f'{titulo:=^40}\n')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'\033[31mErro 404. Não foi possível conectar-se ao site.\033[m')
else:
    print('Site encontrado no servidor WEB.')
