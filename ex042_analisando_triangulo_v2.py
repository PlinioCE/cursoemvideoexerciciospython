titulo = 'TIPO TRIÂNGULO'
print(f'{titulo:=^40}\n')

reta1 = float(input('Digite o comprimento da Reta 1: '))
reta2 = float(input('Digite o comprimento da Reta 2: '))
reta3 = float(input('Digite o comprimento da Reta 3: '))

trianguloValido = reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2)
trianguloEquilatero = reta1 == reta2 == reta3
trianguloIsoceles = reta1 == reta2 or reta1 == reta3 or reta2 == reta3
trianguloEscaleno = reta1 != reta2 != reta3 != reta1

if trianguloValido and trianguloEquilatero:
    tipo = 'formam um TRIÂNGULO EQUILÁTERO'
elif trianguloValido and trianguloIsoceles:
    tipo = 'formam um TRIÂNGULO ISÓCELES'
elif trianguloValido and trianguloEscaleno:
    tipo = 'formam um TRIÂNGULO ESCALENO'
else:
    tipo = 'NÃO FORMAM UM TRIÂNGULO'
print(f'\nA 3 retas combinadas {tipo}.')
