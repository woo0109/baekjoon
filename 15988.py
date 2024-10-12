t = int(input())
dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in range(t):
    print(dp[int(input())-1])