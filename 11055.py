n = int(input())
A = list(map(int, input().split()))
dp = [0] * n
dp[0] = A[0]

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + A[i], dp[i])
        else:
            dp[i] = max(dp[i], A[i])

print(max(dp))