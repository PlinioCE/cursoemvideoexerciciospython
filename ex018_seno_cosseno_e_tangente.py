import math

titulo = 'CalcÂngulo'
print(f'{titulo:=^40}\n')

angulo = float(input('Digite o ângulo (º): '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('\nValores obtidos:\nSen{}º ~ {:.2f}\nCos{}º ~ {:.2f}\nTan{}º ~ {:.2f}'.format(angulo, seno, angulo, cosseno, angulo, tangente))
