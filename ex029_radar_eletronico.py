titulo = 'App RodoVia'
print(f'{titulo:=^40}\n')

limite = int(input('Qual o limite de velocidade da via(Km/h)? '))
velocidade = int(input('Qual a velocidade atual? '))

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('\nVocê ultrapassou o limite de velocidade de {}Km/h!'.format(limite))
    print('Você será multado em R$ {:.2f}.'.format(multa))
else:
    print('\nVocê está dentro do limite de velocidade da via!')
    print('Continue conduzindo com responsabilidade!')
