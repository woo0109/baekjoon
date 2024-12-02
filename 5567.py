import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph):
    cnt = 0
    queue = [1]
    visited[1] = 1

    for _ in range(2):
        next_level = []
        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    cnt += 1
                    next_level.append(neighbor)
        queue = next_level
    return cnt

result = bfs(graph)
print(result)
