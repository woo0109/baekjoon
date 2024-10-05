N, X = map(int, input().split())
n_list = list(map(int, input().split()))
for  i in range(0,N):
    if n_list[i] < X:
        print(n_list[i])