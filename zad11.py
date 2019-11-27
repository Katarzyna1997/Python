a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
if len(a) == len(b):
    result = sum([a[i] * b[i] for i in range(len(a))])
    print('Scalar product:  {} o {}  =  {}'.format(a, b, result))
else:
    print('Wrong dimension vectors!')
