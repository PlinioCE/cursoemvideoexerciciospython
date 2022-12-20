titulo = 'Função Notas'
print(f'{titulo:=^40}\n')


def notas(*numeros, situacao=False):
    """
    -> Programa lê notas de alunos, adiciona a um dicionário e exibe na tela.
    :param numeros: Notas informadas;
    :param situacao: Exibe se o aluno está aprovado, em recuperação ou reprovado;
    :return: Retorna o dicionário.
    """
    alunos = {}
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    if situacao:
        if media >= 7:
            situacao = 'APROVADO'
        elif 4 <= media < 7:
            situacao = 'RECUPERAÇÃO'
        else:
            situacao = 'REPROVADO'
    if not situacao:
        for c in numeros:
            alunos = {'TOTAL': len(numeros), 'MAIOR': maior, 'MENOR': menor, 'MÉDIA': media}
    else:
        for c in numeros:
            alunos = {'TOTAL': len(numeros), 'MAIOR': maior, 'MENOR': menor, 'MÉDIA': media, 'SITUAÇÃO': situacao}
    return alunos


resp = notas(5.5, 2.5, 8.5, situacao=True)
print(resp)
help(notas)


# Resolução Curso em Vídeo


'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita vários valores);
    :param sit: valor opcional, indicando se deve ou não adicionar a situação;
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
print(help(notas()))'''
