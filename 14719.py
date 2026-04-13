h, w = map(int,input().split())
wall = list(map(int, input().split()))
count = 0


for i in range(1, w - 1):
    left_max = max(wall[:i])
    right_max = max(wall[i:])

    if wall[i] <= min(left_max, right_max):
        count += min(left_max, right_max) - wall[i]

print(count)