from ex109_formatando_moedas import moeda

numero = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(numero)} = {moeda.metade(numero, True)}')
print(f'O dobro de {moeda.moeda(numero)} = {moeda.dobro(numero, True)}')
print(f'Aumentando em 10%, {moeda.moeda(numero)} = {moeda.aumentar(numero, 10, True)}')
print(f'Diminuindo em 13%, {moeda.moeda(numero)} = {moeda.diminuir(numero, 13, True)}')
