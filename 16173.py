n = int(input())
arr = []
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

def dfs(x, y):
    visited[x][y] = 1

    dx = [arr[x][y], 0]
    dy = [0, arr[x][y]]

    for i  in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if (nx >= 0 and nx <n) and (ny >= 0 and ny < n) and visited[nx][ny] == 0:
            dfs(nx,ny)


dfs(0,0)

if visited[n-1][n-1] == 1:
    print("HaruHaru")
else:
    print("Hing")