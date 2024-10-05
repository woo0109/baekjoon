N, M = map(int, input().split())
n_list = [0]*N
x = 0
for i in range(0,N):
    n_list[i] = i+1
for i in range(0,M):
    a, b = map(int, input().split())
    x = n_list[a-1]
    n_list[a-1] = n_list[b-1]
    n_list[b-1] = x
for i in range(0,N):
    print(n_list[i])