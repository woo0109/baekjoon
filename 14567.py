import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [1] * n
pre = []

for _ in range(m):
    a,b = map(int, input().split())
    pre.append((a, b))

pre.sort()

for i, j in pre:
    if dp[i-1] + 1 > dp[j-1]:
        dp[j-1] = dp[i-1] + 1

print(*(dp))