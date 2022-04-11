from random import randint
from time import sleep
user = int(input('Choose a number:'))
pc = randint(0, 5)
print('PROCESSING...'), sleep(1)
if user == pc:
  print('Well done, you win!)
else:
        print('Unfortunately, you lost...')
                   
