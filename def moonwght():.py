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
