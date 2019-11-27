import random

N = 128

# Matrix a
a = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        a[i][j] = random.randint(0, 10)
# Matrix b
b = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        b[i][j] = random.randint(0, 10)
# Matrix c
c = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        c[i][j] = a[i][j] + b[i][j]
print(a)
print(b)
print(c)
