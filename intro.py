import time
print('hello guys , today we are going to play a game of mafia . but it is very simple . the only rule in the game is none other than MAFIA . because the code is extremely hard  XD ...')
time.sleep(1)
print('Note:please make sure to fill the informations carefuly . otherwise the game will be messed up. and make sure to play with at least 6 players ...')
time.sleep(1)
print('ANYWAYS lets jump right into the game')
time.sleep(1)
a = int(input('tell me how many players do you have ???')) #کل اعضا
b = int(input('so then , how many mafias do you want for this specific game???')) # مافیا
c = a - b  # شهروند
print('okey . tell me the name of your players... ')
i = 1
l = []
L = []
l_l = []
l_L = []
L_L = []

while i < a + 1 :
 p_p = f'player number {i} :'
 player = input(p_p)
 l.append(player)
 L.append(player)
 l_l.append(player)
 l_L.append(player)
 L_L.append(player)
 i = i + 1
print('okey now . let me randomly choose the mafias.....')

i = 0
o = 0
l_m = []
l_c = L
l_c_t = l_l 
l_m_t = []
K = 0.89568
while i < b :
 t = int(time.time())
 R = ( t%10)
 while R > a - 1:
   R = R - 1
 i = i + 1
 l_m.append(l[R])
 l_m_t.append(l[R])
 l_c.remove(l[R])
 l_c_t.remove(l[R])
 K = K +1.76
 time.sleep(K)
print(' okey . i have decided . LET THE GAMES BEGIN')
print('now i am going to tell the rules . i will call the person and that person is only allowed to look at the monitor . other than that the game will be ruined .')
print('whenever i tell the rule to a person that i called , then that person should tell everyone to open their eyes so then the next person can see their rule')
time.sleep(21)

i = 0
while i < a :
 print(l[i])
 time.sleep(8)
 if l[i] in l_c :
  print(l[i],' . you are a citizen')
 else :
  print(l[i],' . you are a MAFIA')
 i = i + 1
 time.sleep(1.75)
 c = 0
 while c < 500 :
  print()
  c = c + 1 

print('OK this is the first night . everybody sleep . ')
time.sleep(3)
print("its time for the mafia to meet each other  . the MAFIA gang ... WAKE UP ")
time.sleep(4)
print('i will give you guys 10 seconds to meet each other')
time.sleep(6)
print(' CHOP CHOP')
time.sleep(7)
print('times up . the MAFIA GANG , sleep')
time.sleep(3)
print( 'the first night is over . EVERYBODY WAKE UP')
time.sleep(5)



print( 'this is the first day .')
time.sleep(4)
i = 0 
while i < a :
  print(f'{l[i]} . start speaking...you have 20 seconds')
  time.sleep()
  # a = input(str('if the player is done then type (stop)'))
  i = i + 1
  print('your time is over . please stop speaking')
  time.sleep(3)

print('ALLRIGHT . everybody have done their speech . so the first day is also over')
time.sleep(2.5)

looper = 1
N = 2
while looper == 1 :
 print('everybody sleep ')
 time.sleep(1)
 print(f'it is night number { N }')
 print('the mafia should wake up now')
 print(l_c)
 death = input('tell me who do you want to kill tonight bitween theese players?(make sure to type the name right)   ')
 l_c.remove(str(death))
 l.remove(str(death))
 print(f'{str(death)} has been eliminated . now you should sleep . i will give you two seconds to sleep ...')
 time.sleep(3)
 N += 1
 if len(l_m) >= len(l_c) :
  print(f'OK guys . its the day number { N } ...')
  time.sleep(3)
  print(f'last night . {str(death)} has been eliminated ...')
  time.sleep(3)
  print('AND THE MAFIA WON ')
  time.sleep(2)
  print('congragulations to the mafia gang :')
  time.sleep(1)
  print(l_m_t)
  exit()
 else :
  print(f'ok this this the day number {N} . and in the last night...')
  time.sleep(3)
  print(f'last night . {str(death)} was eliminated')
  time.sleep(3)
  print(' AND THE GAME CUNTINIUES')
  time.sleep(2)
  print('its time for you guys to speak...')
  time.sleep(2)
  delay = 0
  j = 0
  while j < a :
   if L_L[j] in l_c :
    print(f'{L_L[j]} . please start speaking . you have 37 seconds')
    time.sleep(delay)
    print('ok . your time is over ...')
    time.sleep(2)
    j = j + 1
   elif L_L[j] in l_m :
    print(f'{L_L[j]} . please start speaking . you have 37 seconds')
    time.sleep(delay)
    print('ok . your time is over ...')
    time.sleep(2)
    j = j + 1 
   else :
    j = j + 1 
 print('okey everyone have done their speaches again ...')
 time.sleep(4)
 print('its time for you guys to vote for the elimination of a person ...')
 time.sleep(3)
 votes = []
 for x in range(len(l)) :
  for y in range(len(l)) :
    if l[y] != l[x] :
      print(f'{l[y]} are you going to vote for {l[x]} ? (yes or no)')
      t_vote = input()
      if 'yes' in t_vote :
        votes.append(l[x])
  for i in range(11) :
   print()
 svotes = list(dict.fromkeys(votes))
 nvotes = []
 for i in range(len(svotes)) :
  nvotes.append(votes.count(svotes[i]))
 h = 0
 print(svotes)
 print(nvotes)
 for i in range(len(nvotes)):
  if h <= nvotes[i] :
   h = nvotes[i] 
 time.sleep(3)
 if h >= len(l)/2 :
  l.remove(svotes[i])
  if svotes[i] in l_m :
   l_m.remove(svotes[i])
  else :
   l_c.remove(svotes[i]) 
  print(f'{svotes[i]} has been voted out...') 
  print(l_m,l_c)
  time.sleep(3)
  if l_m >= l_c :
   print('AND THE MAFIA WON')
   time.sleep(2.5)
   print('congragulations to the mafia gang :')
   time.sleep(1)
   print(l_m_t) 
   exit()
  if l_m < l_c:
   if len(l_m) == 0 :
    print('AND THE CITIZEN WON')
    time.sleep(2)
    print('these were the gang of MAFIA :')
    time.sleep(1)
    print(l_m_t)
    exit()    
   else :
    print('AND THE GAME CUNTINIUES') 
    time.sleep(2)
    print('now SLEEP...')
    
 else :
  print('no one has been voted out . NOW SLEEP...') 
 time.sleep(3) 
 N = N + 1