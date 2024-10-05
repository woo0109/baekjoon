N, M = map(int, input().split())
board = []
chess = []

for i in range(N):
    board.append(input())

for a in range(N-7):
    for b in range(M-7):
        sw = 0
        sb = 0

        for i in range(a,a+8):
            for j in range(b, b+8):

                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        sw += 1
                    if board[i][j] != 'B':
                        sb += 1
                else:
                    if board[i][j] != 'B':
                        sw += 1
                    if board[i][j] != 'W':
                        sb += 1
        chess.append(min(sw, sb))

print(min(chess))