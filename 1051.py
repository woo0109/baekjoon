n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(input()))

small = min(n,m)
size = 0

for i in range(n):
    for j in range(m):
        for k in range(small):
            if ((i+k) < n) and ((j+k) < m) and (arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]):
                size = max(size, (k+1)**2)
print(size)