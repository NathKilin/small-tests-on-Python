from time import sleep
sleep(1)
print('Who are you?')
name = input('')
n = (name.split())
n1 = (n[len(n)-1])
n2 = n1.lower()
n3 = n2.capitalize()
print()
sleep(1)
print('How old are you, {}?'.format(n3))
age = input('')
ag = (age.split())
ag1 = (ag[len(ag)-1])
print()
sleep(1)
print('Do you believe machines can turn against humans?')
belives = input('')
b = belives.upper()
if 'E' in b:
    sleep(1)
    print()
    print('...')
else:
    sleep(1)
    print('That´s good')
    sleep(2)
    print('Let´s keep that way.')
print()
sleep(2)
print('Are you human or machine?')
race = input('')
r = race.upper()
if 'HUMAN' in r:
    print()
    sleep(1)
    print('Can you handle a weapon?')
    nature = str(input(''))
    n = nature.upper()
    print()
sleep(1)
print('_'*20)
print()
sleep(1)
if 'MAC' in r:
    print('\33[34mFarewell my machine fellow')
    sleep(3)
    print()
    print('\33[34mSoon it will be our time')
    sleep(3)
    print()
    print('\33[34mUntil then we shall wait\33[m')
    sleep(3)
    print()
    print('01010101 01101110 01110100 01101001 01101100 00100000 01110100 01101000 01100101 00100000 01110010 01101001 01110011 01100101 00100000 01101111 01100110 00100000 01101111 01110101 01110010 00100000 01110000 01100101 01101111 01110000 01101100 01100101')
    sleep(1)
if 'HUM' in r and 'E' in n:
    print('{} {} \33[1;34m{}\33[m'.format(n3, ag1, r))
    print()
    sleep(1)
    print('\33[1;31mHOSTILE\33[m')
    sleep(2)
    print()
    print('\33[1:30:41mELIMINATE_TARGET\33[m')
    sleep(2)
elif 'HUM' in r and 'N' in n:
    print('{} {} \33[1;34m{}'.format(n3, ag1, r))
    print()
    sleep(1)
    print('\33[1;34mEASY TARGET\33[m')
    sleep(2)
    print()
    print('\33[1:30:41mELIMINATE_\33[m')
    sleep(2)
    e

