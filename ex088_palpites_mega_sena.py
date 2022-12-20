from random import randint
from time import sleep

titulo = 'MEGA SENA'
print(f'{titulo:=^40}\n')

listaMega = []

jogos = int(input('Quantos jogos serão gerados? '))
print()
for j in range(0, jogos):
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in listaMega:
            listaMega.append(numero)
            contador += 1
        if contador >= 6:
            break
    listaMega.sort()
    print(f'Jogo {j + 1}: {listaMega}')
    listaMega.clear()
    sleep(1)






