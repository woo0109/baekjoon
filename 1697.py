from collections import deque

def hide_and_seek():
    n, k = map(int, input().split())

    MAX = 100001
    dist = [-1] * MAX
    dist[n] = 0
    queue = deque([n])

    while True:
        now = queue.popleft()

        if now == k:
            print(dist[now])
            break

        for next in (now - 1, now + 1, now * 2):
            if 0 <= next < MAX and dist[next] == -1:
                dist[next] = dist[now] + 1
                queue.append(next)
    
hide_and_seek()