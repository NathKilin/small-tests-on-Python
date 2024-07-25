#minha lista de compras#
lista = ['tomate', 'alface', 'cebola']
quantidade = [4, 2, 5]
quant_atual = []
lit_final = []
print('Digite a quantidade em estoque dos seguintes itens:')
for n in range(0, len(lista)):
        quant_atual = int(input(f'''\33[1m{lista[n]}\33[m: 
'''))
        if quant_atual < quantidade[n]:
            lit_final.append({lista[n], quantidade[n] - quant_atual})
print('Sua lista está pronta:')
print()
print('{:^120}'.format('Lista de Compras'))
for n in lit_final:
    print(f'{n}')
#print(f'Você precisa de {lit_final}')
#print(quantidade[n])
