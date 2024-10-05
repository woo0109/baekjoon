n = int(input())
num = int(input())
snail = [[0]*n for _ in range(n)]

x, y = (n-1)//2, (n-1)//2
snail[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

i = 2
length = 1
direction = 0

while i <= n*n:
    for _ in range(2):
        for _ in range(length):
            if i > n*n:
                break
            x += dx[direction]
            y += dy[direction]
            
            snail[x][y] = i
            i+= 1
        direction = (direction + 1) % 4
    length += 1
cnt = 1
for row in snail:
    print(*row)
    if num in row:
        numx = cnt
        numy = int(row.index(num)) + 1
    cnt+=1

print(numx, numy)