from random import  randint
from time import  sleep
import  emoji

quantidade_mesas_2 = 6
quantidade_mesas_4 = 4
mesas_2_cheias = randint(0,6)
mesas_4_cheias = randint(0,4)
mesas_4_disponíveis = quantidade_mesas_4 - mesas_4_cheias
mesas_2_disponíveis = quantidade_mesas_2 - mesas_2_cheias
total_mesas_disponíveis = mesas_2_disponíveis + mesas_4_disponíveis
menu = '''
Spagetti -   21,99
Hamburguer - 27,99
Pizza -      25,99
Água -        3,99
Suco -        6,99
Pepsi -       7,99
'''
quando_trazer_o_cardápio = ''
reserva = str(input('Bem-vindo ao Fabuloso e Elegante Restaurante do Nathan. Você fez uma reserva? ')).strip().upper()
if 'SI' in reserva or 'FIZ' in reserva or 'CLARO' in reserva or 'OBV' in reserva or 'ÓBV' in reserva:
    print('Excelente.')
    quantos = str(input('Mesa para quantos? ')).lower().strip()
    if 'doi' in quantos or '2' in quantos or 'dua' in quantos or 'casal' in quantos or '1' in quantos or 'um' in quantos:
        mesas_2_cheias -= 1
        print('Deixe-me te acompanhar até sua mesa ')
    if 'quat' in quantos or '4' in quantos or '3' in quantos or 'tr' in quantos:
        mesas_4_cheias -= 1
        print('Deixe-me te acompanhar até sua mesa ')
    if 'sei' in quantos or '6' in quantos or 'cin' in quantos or '5' in quantos:
        mesas_4_cheias -= 1
        mesas_2_cheias -= 1
        print('Deixe-me te acompanhar até sua mesa')
    if 'set' in quantos or '7' in quantos or 'oit' in quantos or '8' in quantos:
        mesas_4_cheias -= 2
        print('Deixe-me te acompanhar até sua mesa')
if 'N' in reserva or 'ESQUEC' in reserva:
    print('hummm')
    quantos = str(input('Mesa para quantos? ')).lower().strip()
    if total_mesas_disponíveis > 0:
        if 'doi' in quantos or '2' in quantos or 'dua' in quantos or 'casal' in quantos or '1' in quantos or 'um' in quantos:
            if mesas_2_disponíveis > 0 or mesas_4_disponíveis > 0:
                print(f'Temos {mesas_2_disponíveis} mesas disponíveis para vocês')
            elif mesas_2_disponíveis == 0 and mesas_4_disponíveis > 0:
                print('Estamos sem mesas disponíveis mas posso lhe arranjar uma mesa maior se desejar.')
        if 'quat' in quantos or '4' in quantos or '3' in quantos or 'tr' in quantos:
            if mesas_4_disponíveis > 0:
                print(f'Temos {mesas_4_disponíveis} mesas disponíveis para vocês')
            elif mesas_4_disponíveis == 0:
                esperar = str(input('Desculpe, estamos num momento sem mesas disponíveis. Gostaria de esperar no bar? ')).strip().upper()
                if 'SI' in esperar:
                    print('Ótimo! Te avisarei quando houverem mesas disponíveis')
                    sleep(12)
                    print('Seu dia de sorte. Acabaram de liberar uma mesa')
                elif 'N' in esperar:
                    print('Volte sempre')
                    exit()
        if '5' in quantos or 'cin' in quantos or '6' in quantos or 'sei' in quantos:
            if mesas_4_disponíveis >= 1 and mesas_2_disponíveis >= 1 or mesas_4_disponíveis >= 2:
                print('Deixe-me te acompanhar até sua mesa')
            else:
                esperar = str(input('Desculpe, estamos num momento sem mesas disponíveis. Gostaria de esperar no bar? ')).strip().upper()
                if 'SI' in esperar:
                    print('Ótimo! Te avisarei quando houverem mesas disponíveis')
                    sleep(12)
                    print('Seu dia de sorte. Acabaram de liberar uma mesa')
                elif 'N' in esperar:
                    print('Volte sempre')
                    exit()
        if '7' in quantos or 'set' in quantos or '8' in quantos or 'oit' in quantos:
            if mesas_4_disponíveis >= 2 or mesas_2_disponíveis >= 4:
                print('Deixe-me te acompanhar até sua mesa')
            else:
                esperar = str(input('Desculpe, estamos num momento sem mesas disponíveis. Gostaria de esperar no bar? ')).strip().upper()
                if 'SI' in esperar:
                    print('Ótimo! Te avisarei quando houverem mesas disponíveis')
                    sleep(12)
                    print('Seu dia de sorte. Acabaram de liberar uma mesa')
                elif 'N' in esperar:
                    print('Volte sempre')
                    exit()
    else:
     print('Desculpe, estamos num momento sem mesas disponíveis. Gostaria de esperar no bar? ')
trazer_menu = str(input('Posso te trazer o menu?')).strip().upper()
if 'S' in trazer_menu or 'CLA' in trazer_menu or 'POD' in trazer_menu or 'TRA' in trazer_menu:
    print('Aqui está')
    print(menu)
else:
    print('Me avise quando quiser o cardápio')
    while 'PODE' not in quando_trazer_o_cardápio:
        quando_trazer_o_cardápio = str(input('')).strip().upper()
    print('Aqui está')
    print(menu)




