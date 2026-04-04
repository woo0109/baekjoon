import sys
input = sys.stdin.readline

# n: 동전 종류 수, k: 목표 금액
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp 테이블 초기화 (최대 금액인 k보다 큰 값으로 설정)
dp = [10001] * (k + 1)
dp[0] = 0

# 모든 동전에 대해 반복
for coin in coins:
    # 해당 동전으로 만들 수 있는 금액들(coin원부터 k원까지) 확인
    for i in range(coin, k + 1):
        # 기존 방법과 (현재 동전을 하나 쓴 방법) 중 최솟값 업데이트
        if dp[i - coin] != 10001:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 만약 목표 금액 k를 만들 수 없다면 -1 출력
if dp[k] == 10001:
    print("-1")
else:
    print(dp[k])