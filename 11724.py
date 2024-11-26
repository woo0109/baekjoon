import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node):
    visited[node] = 1
    for i in arr[node]:
        if visited[i] != 1:
            dfs(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 0

for i in range(M):
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    if visited[i] != 1:
        dfs(i)
        count += 1
    
print(count)