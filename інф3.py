g=int(input('Sum put in the bank:'))
w=int(input('expected sum:'))
p=int(input('interest rate:'))
k=0
gw=g

while (gw <= w):
    gp=gw*p/100
    gw=gw+gp
    print("sum in the bank:", round(gw,3))
    k=k+1
    print('year', k)





