import sys
sys.setrecursionlimit(100000)

T = int(input())

def dfs(x,y):
    sheep[x][y] = '.'
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx >= 0 and nx < H) and (ny >= 0 and ny < W):
            if sheep[nx][ny] == '#':
                dfs(nx,ny)

for i in range(T):
    H, W = map(int,input().split())
    sheep = [list(input()) for _ in range(H)]
    count = 0

    for i in range(H):
        for j in range(W):
            if sheep[i][j] == '#':
                dfs(i,j)
                count += 1

    print(count)