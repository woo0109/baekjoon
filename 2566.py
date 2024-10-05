a = []
max = 0
row, col = 0, 0

for i in range(9):
    A = list(map(int, input().split()))
    a.append(A)

for i in range(9):
    for j in range(9):
        if a[i][j] >= max:
            max = a[i][j]
            row = i+1
            col = j+1

print(max)
print(row, col) 