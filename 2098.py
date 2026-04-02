import sys
# 재귀 깊이 제한을 늘려줍니다 (N=16일 때 필수)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

# dp[현재_도시][방문_상태] 형태의 메모장
# N=4라면 dp[4][16] 크기의 행렬이 생김
# -1은 "아직 이 상황을 계산해본 적 없음"이라는 뜻
dp = [[-1] * (1 << N) for _ in range(N)]

def find_path(now, visited):
    # [A] 모든 도시 방문 확인
    # (1 << N) - 1은 이진수로 1이 N개인 상태 (예: 1111)
    if visited == (1 << N) - 1:
        # 마지막 도시(now)에서 다시 시작점(0번)으로 돌아갈 길이 있다면 그 비용 반환
        if W[now][0] > 0:
            return W[now][0]
        # 길이 없으면 무한대 반환해서 이 경로는 탈락시킴
        return INF

    # [B] 메모이제이션 (이미 해본 건 또 안 함)
    # 현재 도시(now)에서 이 방문 도장들(visited)을 찍은 상태가 기록에 있다면
    if dp[now][visited] != -1:
        return dp[now][visited] # 저장된 값을 바로 리턴 (시간 절약의 핵심!)

    # [C] 다음 목적지 찾기
    min_cost = INF # 이번 단계에서 찾을 최소 비용 초기화
    for next_city in range(N):
        # 조건 1: 길이 있고 (W[now][next_city] > 0)
        # 조건 2: 아직 안 가본 도시라면 (not (visited & (1 << next_city)))
        if W[now][next_city] > 0 and not (visited & (1 << next_city)):
            
            # [재귀 호출] 다음 도시로 이동하고, 방문 도장(visited)에 다음 도시 비트를 추가(|)함
            # 돌아온 결과값에 지금 이동 비용(W[now][next_city])을 더함
            cost = find_path(next_city, visited | (1 << next_city)) + W[now][next_city]
            
            # 여러 갈래 길 중에서 가장 싼 비용을 선택
            min_cost = min(min_cost, cost)

    # [D] 기록하기
    # 계산 끝난 최솟값을 메모장에 적어두고 반환
    dp[now][visited] = min_cost
    return min_cost

# 0번 도시에서 출발, 0번 도시 방문 도장(1 << 0 = 1) 찍고 시작!
print(find_path(0, 1 << 0))