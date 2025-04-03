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
time.sleep(0.7)
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
print(city)
time.sleep(2)
ENTER = input('havaght tamoom shod . baraye edame (ENTER) ra bezanid...')
print('khayli khoob . hala bazi shoroo mishavad...')



# game counters
day = 1
night = 1
death = []
mafia_death = []
city_death = []
karagah_death = []
doctor_death = []
tak_tir_death = []


#the first night
print(f'shabe aval :')
time.sleep(1)
print('mafia ha bidar shavand va be modat 10 sanie ba hamdigar ashna mishavand...')
time.sleep(10)
print('vagt tamam shod . hala mafia bekhabad ...')
time.sleep(3)
print('shab aval tamam shod . hala sobh aval shoroo mishavad...')
time.sleep(2)
night += 1


# the first day
print(f'sobh aval :')
time.sleep(1)
print('shahvand ha bidar shavand va be modat 15 sanie ba hamdigar ashna mishavand...')
time.sleep(6)
for i in range(len(players)):
    print(f'bazikon shomare {i + 1} : 15 sanie sohbat darad...')
    time.sleep(0)
    print('vaght tamam shod...')
    time.sleep(2)
print('rooz aval tamam shod . hala shab dovom shoroo mishavad...')
time.sleep(2)
day += 1


# game loop
while True:


    # night
    print(f'shabe {night} :')
    time.sleep(1)
    print('mafia ha bidar shavand va az mian shahrvand ha yeki ra bayar koshtan entekhab konnand...')
    print(only_city)
    time.sleep(2)
    kill_choice = input('esm bazikoni ra ke mikhahid bokoshid vared konid : ')
    while kill_choice not in only_city:
        kill_choice = input('esm bazikon ra DOROST vared konid : ')
    while kill_choice in mafia:
        kill_choice = input('mafia nemitavanad khodash ra bokoshad . lotfan yek shahrvand ra entekhab konid : ')
    while kill_choice in death:
        kill_choice = input('in shahrvand ghablan koshte shode ast . lotfan yek shahrvand digar ra entekhab konid : ')
    death.append(kill_choice)
    city_death.append(kill_choice)
    only_city.remove(kill_choice)
    time.sleep(2)
    print(only_city)
    print(death)
