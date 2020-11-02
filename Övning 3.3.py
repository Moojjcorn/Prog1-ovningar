import math
a = float(input('Ange sida As längd: '))
b = float(input('Ange sida Bs längd: '))
alfa = float(input('Ange vinkels grad tal: '))

x = a**2+b**2-2*a*b*math.cos(alfa)
c = math.sqrt(x)

likSidig = a-b-c
likBent = a-b
if likBent == 0:
    print(f'Trianglen är likbent! {c:.2f}')
else:
    if likSidig == 0:
        print(f'Trianglen är liksidig! {c:.2f}')
    else:
        print(f'Trianglen är oliksidig! {c:.2f}')
