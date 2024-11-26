N = int(input())
arr = []
cnt = 0

for i in range(N):
    a = int(input())
    arr.append(a)

for i in range(1,N):
    while arr[-i-1] >= arr[-i]:
        arr[-i-1] -= 1
        cnt += 1

print(cnt)