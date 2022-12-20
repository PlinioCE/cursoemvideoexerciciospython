titulo = 'BANCO SAQUE'
print(f'{titulo:=^40}\n')

valorSaque = int(input('Qual valor deseja sacar? R$ '))
print('================================')
if valorSaque >= 50:
    notas50 = valorSaque // 50
    resto50 = (valorSaque - (notas50 * 50))
    notas20 = resto50 // 20
    resto20 = resto50 - (notas20 * 20)
    notas10 = resto20 // 10
    resto10 = resto20 - (notas10 * 10)
    notas1 = resto10 // 1
    resto1 = resto10 - (notas1 * 1)
    if notas50 <= 1:
        print(f'{notas50} nota de R$ 50.00')
    else:
        print(f'{notas50} notas de R$ 50.00')
    if resto50 >= 20:
        if notas20 <= 1:
            print(f'{notas20} nota de R$ 20.00')
        else:
            print(f'{notas20} notas de R$ 20.00')
    if resto50 > 10 or resto20 > 10:
        if notas10 == 1:
            print(f'{notas10} nota de R$ 10.00')
        else:
            print(f'{notas10} notas de 10.00')
    if resto50 < 10 or resto20 < 10 or resto10 < 10:
        if notas1 == 1:
            print(f'{notas1} nota de R$ 1.00')
        elif notas1 > 1:
            print(f'{notas1} notas de R$ 1.00')
print('================================')
print('CONFIRA SEU DINHEIRO!')

# Resolução Curso em Vídeo

'''valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'{totalCedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre e tenha um bom dia!')'''
