times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo',
         'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
         'Atlético-GO', 'Avaí', 'juventude')
print(times)
print('=-' * 20)
print(f'Os cinco primeiros colocados do campeonato são: {times[0:5]}')
print('=-' * 20)
print(f'Os quatro últimos colocados são: {times[16:20]}')
print('=-' * 20)
print(f'Times em ordem alfabétic: {(sorted(times))}')
print('=-' * 20)
print(f"O São Paulo está na {times.index('São Paulo') + 1 } colocação")