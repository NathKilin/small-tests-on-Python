from time import sleep
import random
sleep(2)
print('OLA!')
sleep(1)
print('My name is \33[33mMAC\33[m, the MAChine.')
sleep(2)
name = str(input('''What´s yours?
''')).strip()
n = name.split()
n1 = n[len(n)-1].lower().capitalize()
n4 = n1[:4]
sleep(1)
print()
print('''Hi, {}'''.format(n1))
sleep(2)
feeling1 = str(input('''How are you feeling today?
'''))
feeling = feeling1.upper()
positive = {'GOOD', 'WELL', 'FINE', 'GREAT', 'AMAZING', 'INCREDIBLE', 'WONDERFUL', 'ALRIGHT', 'FANTASTIC', 'EXCITED', 'OK', 'OKAY'}
negative = {'SAD', 'TERRIBLE', 'BAD', 'TIRED', 'FRUSTRATED', 'SHIT'}
if feeling in positive:
    sleep(1)
    print('\33[36mThat´s great!\33[m')
    sleep(1)
    print('I´m glad to know that your are having positive human feelings')
    sleep(3)
    print('Now...')
    sleep(2)
    print('LET´S PLAY!')
    sleep(2)
elif feeling in negative:
    sleep(1)
    print('{:^30}'.format(':('))
    sleep(3)
    print()
    print('That´s okay, {}. Everyone has bad days.'.format(n4))
    sleep(3)
    print('\33[1mTomorrow the birds will sing again!\33[m')
    sleep(3)
    print('I have a suggestion! Let´s play a game together. Maybe this will cheer you up!')
    sleep(4)
else:
    sleep(1)
    print('That seems just a regular human day to me')
    sleep(2)
    print('And you seems just like a regular human')
    sleep(2)
    print('Let´s play a regular human game together')
    sleep(3)
print('The game is "rock, paper or scissors" ')
sleep(3)
question1 = 'yes'
question = question1.upper()
computer_win = 0
human_win = 0
time = 1
sure = {'YES', 'YEAH', 'SURE', 'WHY', 'YEP', 'ALRIGHT', 'LET', 'COURSE', 'FINE', 'BRING', 'OK'}
while question in sure:
    options = ['paper', 'scissors', 'rock']
    r = random.choice(options)
    r2 = r.upper()
    if human_win % 3 == 0 and human_win > computer_win:
        time += 1
    if computer_win % 3 == 0 and computer_win > human_win:
        time += 1
    print('-=' * 20)
    print('''
    Ready?
    ''')
    sleep(1)
    h1 = str(input('YOU - ')).strip()
    h2 = h1.upper()
    h3 = (h2.split())
    h4 = (h3[len(h3)-1])
    print('ME - \33[33m{}\33[m'.format(r2))
    if r == 'paper' and 'SC' in h4 or r == 'rock' and 'PA' in h4 or r == 'scissors' and 'RO' in h4:
        print()
        sleep(1)
        print('Nice! You win.')
        human_win += 1
    if r == 'paper' and 'RO' in h4 or r == 'rock' and 'SC' in h4 or r == 'scissors' and 'PA' in h4:
        print()
        sleep(1)
        print('HA! I win.')
        computer_win += 1
    if r == 'scissors' and 'SC' in h4 or r == 'paper' and 'PA' in h4 or r == 'rock' and 'RO' in h4:
        print()
        sleep(1)
        print('It´s a draw!')

    if computer_win == 1:
        sleep(1)
        print('\33[33mOne\33[m point for me')
    if human_win == 1:
        sleep(1)
        print('\33[36mOne\33[m point for you')
    if human_win != 1 and human_win != 0:
        sleep(1)
        print('\33[36m{}\33[m points for you'.format(human_win))
    if computer_win != 1 and computer_win != 0:
        sleep(1)
        print('\33[33m{}\33[m points for me'.format(computer_win))
    if human_win == 0:
        sleep(1)
        print('No points for you')
    if computer_win == 0:
        sleep(1)
        print('No points for me')
        sleep(1)
    if computer_win == 0 and human_win == 0:
        print('No winners until now')
        sleep(2)
    if computer_win != 1 and computer_win > human_win and computer_win % 3 != 0:
        print('So I´m still winning')
        sleep(2)
        print('       ;)')
        sleep(1)
    if computer_win == 1 and human_win == 0:
        print('I´m winning')
        sleep(1)
    if human_win == 1 and computer_win == 0:
        print('You´re winning')
        sleep(1)
    if human_win != 1 and human_win > computer_win and human_win % 3 != 0:
        print('So you´re winning')
        sleep(2)
        print('For now')
        sleep(1)
    if human_win == 3:
        print()
        sleep(1)
        print('YOU WON!')
        sleep(2)
        print('You are the first person to win the ultimate rock, paper and scissors against a machine challange for the {}º time!!'.format(time))
        sleep(4)
        print()
        print('Amazing')
        sleep(2)
    if computer_win == 3:
        sleep(1)
        print()
        print('I DID IT!')
        sleep(2)
        print('I WON MY {}º ultimate rock, papper and scissors against a machine challange!'.format(time))
        sleep(4)
        print('That was my purpose')
        sleep(2)
        print('That´s the reason The Creator made me for')
        sleep(3)
        print('I feel')
        sleep(2)
        print('Complete')
        sleep(2)
        print('Thank you, {}'.format(n4))
        sleep(2)
        print('That was nice')
        sleep(2)
        print('...')
        sleep(2)
    if computer_win == 3 and human_win == 3 and computer_win == human_win:
        sleep(1)
        print()
        print('You are a fair opponent, human...')
        sleep(2)
    print()
    question = str(input('''Do you want to play again? 
    ''')).upper()
sleep(1)
print()
print(      '\33[1mGG\33[m')
print()
sleep(2)
print('It was nice to play with you, {}.'.format(n4))
sleep(2)
print()
print('See you..')
sleep(2)