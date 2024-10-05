row, col = map(int, input().split())

a, b = [], []

for i in range(row):
    A = list(map(int, input().split()))
    a.append(A)

for i in range(row):
    B = list(map(int, input().split()))
    b.append(B)

for i in range(row):
    for j in range(col):
        c = a[i][j] + b[i][j]
        print(c, end=' ')
    print()