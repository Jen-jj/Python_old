def money(x, y, i):
    return x + y - i
x = 7
y = 8
i = 9
print(money(x, y, i))
def sayhi(name):
    print('hi %s' % name)
sayhi('joe')
def myfuntion(t1, t2, t3):
    return t1 + t2 + t3
x = myfuntion(10, 45, 78)
print(x)
def tr_bd(wheels):
    intt = 0
    for week in range(1, 53):
        intt = intt + wheels
        print('week %s = %s wheels' % (week, intt))
print(tr_bd)