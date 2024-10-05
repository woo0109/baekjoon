n, m = map(int,input().split())
xl = list(map(int,input().split()))
sum = []
answer = []

for i in range(n):
    for j in range(i+1,n,1):
        for k in range(j+1,n,1):
            total = xl[i]+xl[j]+xl[k]
            sum.append(total)

for i in range(len(sum)):
    if sum[i]<=m:
        answer.append(sum[i])

print(max(answer))