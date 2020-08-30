class alive:
    pass
class an(alive):
    def breathe(self):
        print('hhh')
    def suffct(self):
        self.breathe()
        self.breathe()
rej = an()
rej.suffct()
fruits = ['apple', 'banan', 'troll']
number = len(fruits)
for x in range(0, number):
    print('fruit number %s is %s' % (x, fruits[x]))
ttt = list(range(0, 30, 2))
print(ttt)
class animal:
    def __init__(self, colour, species):
        self.species = species
        self.colour = colour

import copy
dia = animal('pink', 'fluffy')
dian = copy.copy(dia)
print(dia.colour)
print(dian.colour)
import keyword
print(keyword.iskeyword('if'))
import random
print(random.randint(1, 100))
import random
number = random.randint(1, 100)
import random
desserts = ['brownies', 'cookies', 'cinema rolls'] 
print(random.choice(desserts))
random.shuffle(desserts)
print(desserts)
import time
print(time.time())
def lon(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print("i`ll need %s seconds" % (t2-t1))
lon(100)
for x in range(1, 61):
    print(x)
    time.sleep(1)
favorith = {'music':['billie holiday', 'conan gray'], 
'clothes':['chanel', 'skirts']}
import pickle
favorith = {'music':['billie holiday', 'conan gray'], 
'clothes':['chanel', 'skirts']}
file = open('save.dat', 'wd')
pickle.dump(favorith, file)
file.close()
sf = open('save.dat', 'rb')
fvr = pickle.load(sf)
