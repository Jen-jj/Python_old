import time
print(time.asctime())
import sys
print(sys.stdin.readline())
def stupidage(age):
    if age < 16:
        print('go home go to jail')
    else:
        print('welcome')
stupidage(15)
wgt = 49
for yr in range(1, 14):
    wgt = wgt + 1
    moonwgt = wgt * 0.165
    print('yr %s your moon wgt %s' % (yr, moonwgt))
def moonwgt(wgt, plus):
    for yr in range(1, 12):
        wgt = wgt + plus
        moonwgt = wgt * 0.165
        print('year %s Your weight %s' % (yr, moonwgt))
print(moonwgt(49, 0.2))
def moonwgt(wgt, plus, years):
    for yr in range(1, years):
        wgt = wgt + plus
        moonwgt = wgt * 0.165
        print('year %s Your weight %s' % (yr, moonwgt))
print(moonwgt(49, 0.2, 15))

import sys
def moonwght():
    print('type your weight')
    weight = float(sys.stdin.readline())
    print('type your weight gain')
    gain = float(sys.stdin.readline())
    print('type the number of years')
    years = float(sys.stdin.readline())
    years = years + 1
    for yr in range(1, years):
        weight = weight + gain
        print('your moon weight = %s after %s years' % (weight, yr))
