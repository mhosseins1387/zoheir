url = 'https://airnow.tehran.ir/'
import requests
from bs4 import BeautifulSoup

x = requests.get(url)
y = BeautifulSoup(x.text , "html.parser")
def printTo(x):
 if 1<=x<=50 :
 	print('(healthy)')
 if 51<=x<=100 : 
 	print('(acceptable)')
 if 101<=x<=150 :
 	print('(unhealthy<for a special group>)')
 if 151<=x<=200 :
 	print('(unleahthy)')
 if 200<=x<=251 :
 	print('(very unhealthy)')
 if x >= 251  :
 	print('(dangerous)')
x = y.find(['span'], id="ContentPlaceHolder1_lblAqi3h")
print(f'your air 1polution rate is at {x.string} ',end='')
printTo(int(x.string))
p = y.find(['span'],id="ContentPlaceHolder1_lblAqi24h")
print(f'last day it was at {p.string}', end='')
printTo(int(p.string))


