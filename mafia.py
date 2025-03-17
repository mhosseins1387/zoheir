import time


print('slm . be mafia khoosh amadid . ma dar in bazi 5 najsh darim:1.shahvand , 2:mafia , 3:karagah , 4:doctor , 5:taktir andaz')
time.sleep(4)
a = int(input('tedad bazikonan : '))
b = int(input('tedad mafia : '))
c = a - b
players = []
for i in range(a):
    x = input(f'bazikon shomare {i +1} : ')
    players.append(x)
print(players)


