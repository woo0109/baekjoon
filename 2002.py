n = int(input())
before = {}
after = []
cnt = 0

for i in range(n):
    before[input()] = i

for i in range(n):
    after.append(input())

for i in range(n-1):
    for j in range(i+1, n):
        if before[after[i]] > before[after[j]]:
            cnt += 1
            break

print(cnt)