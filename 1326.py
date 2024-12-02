def bfs(a, b, bridge, N):
    if a == b:
        return 0

    queue = [a-1]
    visited = [-1] * N
    visited[a-1] = 0
    
    while queue:
        node = queue.pop(0)
        for n in range(N):
            if bridge[node] > 0 and (n - node) % bridge[node] == 0 and visited[n] == -1:
                queue.append(n)
                visited[n] = visited[node] + 1
                if n == b-1:
                    return visited[n]
    
    return -1

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, bridge, N))
