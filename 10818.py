N = int(input())
n_list = list(map(int, input().split()))
M = -1000000
m = 1000000

for i in range(0,N):
    if n_list[i]>M:
        M = n_list[i]
    if n_list[i]<m:
        m = n_list[i]
print(M,m)