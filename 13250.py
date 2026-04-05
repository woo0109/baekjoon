n = int(input())
dp = [0.0] * (n + 6)

for i in range(n-1, -1, -1):
    total = 0
    for dice in range(1, 7):
        if i + dice < n:
            total += dp[i+dice]
        else:
            total += 0
    dp[i] = total / 6 + 1

print(dp[0])