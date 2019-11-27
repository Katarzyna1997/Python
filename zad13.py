import random

N = 8

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
c = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            c[j][i] += a[i][k] * b[k][j]
            
print(a)
print(b)
print(c)
