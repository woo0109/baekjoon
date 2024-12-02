import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
order = 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort(reverse=True)

def bfs(graph, start):
    global order
    queue = [start]
    visited[start] = order
    order += 1
    
    while queue:  
        current = queue.pop(0) 
        
        for neighbor in graph[current]:  
            if visited[neighbor] == 0:  
                visited[neighbor] = order
                order += 1
                queue.append(neighbor)  


bfs(graph, r)
for i in range(1, n+1):
    print(visited[i])