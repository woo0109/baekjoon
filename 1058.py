n = int(input())
friend = [list(input()) for _ in range(n)]
connection = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            elif friend[j][k] == 'Y' or (friend[j][i] == 'Y' and friend[i][k] == 'Y'):
                connection[j][k] = 1

cnt = 0
for row in connection:
    cnt = max(cnt, sum(row))

print(cnt)