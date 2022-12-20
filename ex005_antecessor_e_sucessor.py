titulo = str('ANTECESSOR E SUCESSOR')
#print('{:=^40}'.format(titulo))
print(f"{titulo:=^40} \n")

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('\n{} tem como seu antecessor {} e como sucessor {}.'.format(numero, antecessor, sucessor))
print('\n{} tem como seu antecessor {} e como sucessor {}.'.format(numero, (numero - 1), (numero + 1)))
