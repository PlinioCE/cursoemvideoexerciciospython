from ex115_criando_um_menu.lib.interface import *
from ex115_criando_um_menu.lib.arquivo import *
from time import sleep

arquivo = 'lista_pessoas.txt'

if not verifica_arquivo(arquivo):
    cria_arquivo(arquivo)

while True:
    escolha = menu(['Exibir Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if escolha == 1:
        cabecalho('LISTA CADASTRADOS'.center(len(linha())))
        ler_arquivo(arquivo)
    elif escolha == 2:
        cabecalho('NOVO CADASTRO'.center(len(linha())))
        nome = str(input('NOME: ')).strip().title()
        idade = leia_int('IDADE: ')
        cadastra_pessoa(arquivo, nome, idade)
    elif escolha == 3:
        cabecalho('*** FINALIZANDO SISTEMA ***'.center((len(linha()))))
        break
    else:
        print('\033[31mERRO! Informe uma opção válida!\033[m')
    sleep(1)
