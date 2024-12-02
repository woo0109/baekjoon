from collections import deque

t = int(input())

result = []

for _ in range(t):
    n = int(input()) #편의점 개수

    hx, hy = map(int, input().split()) #home
    store = deque()

    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    fx, fy = map(int, input().split()) #페스티벌


    queue = deque()
    queue.append((hx, hy))

    flag = False

    check = n

    while queue:
        nx, ny = queue.popleft()

        if(abs(nx - fx) + abs(ny - fy) <= 1000): #가고싶은 범위 이내에 페스티벌이 있음. 
            result.append(1)
            flag = True
            break
        else: #무조건 편의점 찍고와야함((
            for i in range(len(store)):
                a, b = store.popleft()
                if(abs(nx - a) + abs(ny - b) <= 1000): #범위 이내에 편의점이 있음. 
                    queue.append((a, b))
                else:
                    store.append((a,b))

    if(flag == False):
        result.append(0)

for i in result:
    if(i == 1):
        print("happy")
    else:
        print("sad")