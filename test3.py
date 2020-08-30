for x in range(0, 6):
    print('hi')
print(list(range(10, 20)))
for x in range(0, 5):
    print('hi %s' % x)
x = 0
print('hihi %s' % x)
mymylist = ['fig jam', 'peanut butter', 'milktea']
for i in mymylist:
    print(i)
hairypants = ['hairy', 'pants']
for j in hairypants:
    print(j)
    for i in hairypants:
        print(i)
foco = 20
maco = 70
stco = 3
co = foco
for week in range(1, 53):
    co = co + maco - stco
    print('week %s = %s' % (week, co))
for stairs in range(0, 20):
    print(stairs)
x = 44
y = 56
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
for x in range(0, 20):
    print('hi %s' % x)
    if x > 12:
        break
y = 0
for y in range(0, 30):
    print(y + 2)
    if y + 2 > 12:
        break
x = 1
lunch = ['tomatoes', 'bread', 'cheese', 'jam']
for i in lunch:
    print('%s %s' % (x, i)) 
    x = x + 1
