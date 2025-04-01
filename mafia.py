import time
import random


print('slm . be mafia khoosh amadid . ma dar in bazi 5 nagsh darim:1.shahvand , 2:mafia , 3:karagah , 4:doctor , 5:tak tir andaz')
time.sleep(2.25)
print('dar in bazi shoma mitavanid az 5 nafar bazikon ya bishtar estefade konid va tedad mafia ha bishtar az 1 nafar bashad')
time.sleep(2.75)
print('hala lotfan tedad bazikonan ra vared konid...')
time.sleep(1.75)
a = int(input('tedad bazikonan : '))
if a < 5 :
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


# intruducing the roles
mafia = []
only_city = []
city_all = []
city = []
karagah = []
doctor = []
tak_tir = []
for i in range(a):
    city.append(players[i])
for i in range(a):
    city_all.append(players[i])
for i in range(a):
    only_city.append(players[i])




#generating the roles
for i in range(b):
    x = random.choice(players)
    mafia.append(x)
    city.remove(x)
    only_city.remove(x)

rand = []
for i in range(3):
    x = random.choice(city)
    city.remove(x)
    rand.append(x)
karagah.append(rand[0])
doctor.append(rand[1])
tak_tir.append(rand[2])


# showing the roles
print('khayli khoob . hala nagsh ha pakhsh mishavand...')
print('lotfan ravi bazi nagsh ra bebinid va be bazikonan nagsh hayshan ra begin...')
time.sleep(2)
print('mafia ha :')
print(mafia)
time.sleep(2)
print('karagah :')
print(karagah)
time.sleep(2)
print('doctor :')
print(doctor)
time.sleep(2)
print('tak tir andaz :')
print(tak_tir)
time.sleep(2)
print('tamami shahvand ha :')
print(city_all)
time.sleep(2)