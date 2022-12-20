titulo = 'Valida Triângulo'
print(f'{titulo:=^40}\n')

reta1 = float(input('Digite o comprimento da Reta 1: '))
reta2 = float(input('Digite o comprimento da Reta 2: '))
reta3 = float(input('Digite o comprimento da Reta 3: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('\nCom a combinação das 3 retas é POSSÍVEL formar um triângulo!')
else:
    print('\nCom a combinação das 3 retas é IMPOSSÍVEL formar um triângulo!')
