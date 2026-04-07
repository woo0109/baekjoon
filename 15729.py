n = int(input())

origin = [0] * n
light = list(map(int, input().split()))
count = 0

for i in range(n):
    if origin[i] != light[i]:
        count += 1

        origin[i] = 1 - origin[i]

        if i + 1 < n:
            origin[i+1] = 1 - origin[i+1]
        if i + 2 < n:
            origin[i+2] = 1 - origin[i+2]

print(count)