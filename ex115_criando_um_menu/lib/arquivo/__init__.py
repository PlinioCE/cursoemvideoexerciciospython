def verifica_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print(f'Erro ao tentar criar o arquivo \'{nome}\'.')
    else:
        print(f'Arquivo \'{nome}\' criado!')


def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print(f'Erro ao tentar ler o arquivo \'{nome}\'.')
    else:
        for linha in arquivo:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>5} anos')
    finally:
        arquivo.close()


def cadastra_pessoa(nome, pessoa='Desconhecido', idade=0):
    try:
        arquivo = open(nome, 'at')
    except:
        print(f'Erro ao tentar realizar um novo cadastro em \'{nome}\'.')
    else:
        try:
            arquivo.write(f'{pessoa};{idade}\n')
        except:
            print(f'Erro ao tentar adicionar os dados de {pessoa}.')
        else:
            print(f'{pessoa} adicionado ao cadastro!')
    finally:
        arquivo.close()
