n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = -1

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v):
    visited[v] = 1
    global count
    count += 1
    for i in arr[v]:
        if visited[i] != 1:
            dfs(i)

dfs(1)
print(count)