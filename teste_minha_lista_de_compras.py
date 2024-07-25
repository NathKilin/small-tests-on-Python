listagem = ('Pão', 2, 'arroz', 5, 'feijão', 3, 'batata', 6)
print()
print(f'\33[1m{"Lista de compras":^160}\33[m')
print()
print('{:^160}'.format('=' * 51))
print()
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'\33[33m{listagem[posição]:>66}\33[m', end= '')
        print('.'*30, end='')
    else:
        print(f'{listagem[posição]}')
print()