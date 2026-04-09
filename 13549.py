from collections import deque

def hide_and_seek():
    n, k = map(int,input().split())

    MAX = 100001
    dist = [-1] * MAX

    queue = deque([n])
    dist[n] = 0

    while queue:
        now = queue.popleft()

        if now == k:
            print(dist[now])
            break

        if now * 2 < MAX and dist[now * 2] == -1:
            dist[now * 2] = dist[now]
            queue.appendleft(now * 2)
        
        if 0 <= now - 1 and dist[now - 1] == -1:
            dist[now - 1] = dist[now] + 1
            queue.append(now - 1)
        
        if now + 1 < MAX and dist[now + 1] == -1:
            dist[now + 1] = dist[now] + 1
            queue.append(now + 1)
        
hide_and_seek()