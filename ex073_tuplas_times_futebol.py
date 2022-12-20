titulo = 'TABELA BRASILEIRÃO 2022'
print(f'{titulo:=^40}\n')

times = ('COR', 'CFC', 'PAL', 'SAO', 'SAN',
         'CAM', 'BOT', 'FLU', 'AMG', 'AVA',
         'BRA', 'INT', 'CAP', 'FLA', 'GOI',
         'CUI', 'JUV', 'CEA', 'AGO', 'FOR')
print(f'CLASSIFICADOS À LIBERTADORES: {times[:5]}')
print(f'ZONA DE REBAIXAMENTO: {times[-4:]}')
print(f'TIMES EM ORDEM ALFABÉTICA: {sorted(times)}')
print(f'O Ceará está na {times.index("CEA") + 1}ª colocação.')
