import time


print('slm . be mafia khoosh amadid . ma dar in bazi 5 najsh darim:1.shahvand , 2:mafia , 3:karagah , 4:doctor , 5:taktir andaz')
time.sleep(4)
a = int(input('tedad bazikonan : '))
b = int(input('tedad mafia : '))
if a//2  <= b:
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
    


