N, M = map(int, input().split())
n_list = [0]*N
for i in range(0,M):
    a, b, c = map(int, input().split())
    for j in range(a-1,b):
        n_list[j] = c
for i in range(0,N):
    print(n_list[i])