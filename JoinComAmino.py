import samino
import pyfiglet
import time
import sys
from colorama import init, Fore, Back, Style
init()
c = samino.Client("22E101D71BD9A1F5DF90220C39C6BA59C8339B276B5777FDB9E281F5E0789C09D7709400ACB2875DE5")

Y = "\033[1;33m"
print(Y+pyfiglet.figlet_format("Join com"))
def Animation(text):
	for letter in text + '\n':
	    sys.stdout.write(letter)
	    sys.stdout.flush()
	    time.sleep(15/1000)

Animation(Y+'''
 
  Вход с ботов в - - - > КОМЬЮНИТИ
/---------------------------------\\

              by tek1
     group: t.me/coin_tilted
     github.com/tek1bot
\---------------------------------/
_____________________________________
''')

password = input("password:")
link = input("URL community:")


comId=c.get_from_link(link).comId
for e in open('emails.txt').read().split():
 try:
	c.login(e,password=password)
except:
	continue
 c.join_community(comId)
 print(f'joined completed to'+e)
