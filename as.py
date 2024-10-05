n = int(input())

# n x n 크기의 2차원 리스트 생성
snail = [[0]*n for _ in range(n)]

# 초기 위치: 중심
x, y = (n-1)//2, (n-1)//2
snail[x][y] = 1

# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

i = 2  # 채워질 숫자
length = 1  # 처음에는 1칸 이동
direction = 0  # 처음에는 위로 이동 (dx[0], dy[0] => 상)

# 달팽이 채우기
while i <= n*n:
    for _ in range(2):  # 각 길이를 2번씩 반복 (위-오른쪽, 아래-왼쪽)
        for _ in range(length):
            if i > n*n:  # 숫자가 n*n을 넘으면 종료
                break
            x += dx[direction]  # 방향에 따른 이동
            y += dy[direction]
            snail[x][y] = i  # 숫자 채우기
            i += 1
        direction = (direction + 1) % 4  # 방향을 바꿈
    length += 1  # 이동해야 할 길이를 1씩 늘림

# 결과 출력 (달팽이 배열)
for row in snail:
    print(row)
