titulo = 'Tratamento de Erros e Exceções'
print(f'{titulo:=^40}\n')


def leia_int(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[34mO usuário decidiu não informar o valor inteiro\033[m.')
            return 0
        except Exception as erro:
            print(f'\033[31mERRO: {erro.__class__} / {erro.__cause__}')
        else:
            return f'{n}'.replace('.', ',')


def leia_float(texto):
    while True:
        try:
            n = str(input(texto)).replace(',', '.')
            n = float(n)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[34mO usuário decidiu não informar o valor real.\033[m')
            return 0
        except Exception as erro:
            print(f'ERRO: {erro.__class__} / {erro.__cause__}')
        else:
            return f'{n}'.replace('.', ',')


numero_inteiro = leia_int('Digite um número inteiro: ')
numero_float = leia_float('Digite um número real(fracionado): ')
print(f'\nVocê digitou o número inteiro: \033[32m{numero_inteiro}\033[m')
print(f'Você digitou o número real: \033[32m{numero_float}\033[m')
