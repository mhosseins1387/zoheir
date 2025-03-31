import time


print('slm . be mafia khoosh amadid . ma dar in bazi 5 nagsh darim:1.shahvand , 2:mafia , 3:karagah , 4:doctor , 5:taktir andaz')
time.sleep(4)
a = int(input('tedad bazikonan : '))
if a <= 5 :
    exit('NEMISHE . tedad player ha khayli baray 5 nash darid...')
elif a > 12 :
    exit('NEMISHE . playera ziyadan . had aksar 12 player...')
b = int(input('tedad mafia : '))
if a//3  < b:
    print('NEMISHE . MAFIA ZIADE!!!')
    exit()
c = a - b#city


# taking player's names
players = []
for i in range(1,1+a):
    x = input(f'bazikon shomare {i} : ')
    players.append(x)


# checking player's names
for i in range(len(players)-1):
    for x in range(i+1,len(players)):
        if players[i]==players[x]:
            exit(f'NEMISHE . esm bazikon {i+1} ba bazikon {x+1} yekie...')
time.sleep(0.7)
print('khayli khoob . hala vassta nagsh haro pakhsh konam...')


#generating random numbers
ran = []
r_1 = int(time.time())%10
while r_1 > a - 1:
    r_1 = r_1 - 1
ran.append(r_1)
time.sleep(3.5)
for i in range(b-1):
    r_2 = int(time.time())%10
    if r_2 > a-1 :
        r_2 = r_1 - 2
    ran.append(r_2)
    time.sleep(1.75)
print(ran)
mafia = []
for i in (ran):
    mafia.append(players[i])
print(mafia)
