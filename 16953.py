a, b = map(int,input().split())
count = 1

while a != b:
    if b == 0:
        count = -1
        break
    elif b % 2 == 0:
        b = b / 2
        count += 1
    elif b % 10 == 1:
        b = b // 10
        count += 1
    else:
        count = -1
        break

print(count)