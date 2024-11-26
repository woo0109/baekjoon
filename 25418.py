A, K = map(int, input().split())
cnt = 0

while A != K:
    if K % 2 == 0 and K / 2 >= A:
        K /= 2
        cnt += 1
    else:
        K -= 1
        cnt += 1

print(cnt)