def roots(a=0, b=0, c=0):
    delta = b * b - 4 * a * c
    if delta < 0: return []
    elif delta == 0 : return [ -b / 2 / a ]
    else: return [ (-delta - b) / 2 / a, (delta - b) / 2 / a ]


print('Quadratic equation (e.g.: ax^2 + bx + c = 0): ')
try:
    a = float(input('Enter a parameter: '))
    b = float(input('Enter b parameter: '))
    c = float(input('Enter c parameter: '))
except ValueError:
    print('Enter numbers!')
    import sys
    sys.exit(1)

print('\nResults: ')
roots = roots(a, b, c)
for root in roots: print(root)
if not roots: print('-')
