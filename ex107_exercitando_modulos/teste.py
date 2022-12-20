from ex107_exercitando_modulos import moeda

numero = float(input('Informe o preço: R$ '))
print(f'A metade de {numero} = {moeda.metade(numero)}')
print(f'O dobro de {numero} = {moeda.dobro(numero)}')
print(f'Aumentado em 10%, {numero} = {moeda.aumentar(numero, 10)}')
print(f'Diminuindo em 13%, {numero} = {moeda.diminuir(numero, 13)}')
