n = int(input())
l = []
count = 1

for _ in range(n):
    row = list(map(int, input().split()))
    l.append(row)

l.sort(key = lambda x : (x[1], x[0]))
fin = l[0][1]

for i in range(n-1):
    if fin <= l[i+1][0]:
        count += 1
        fin = l[i+1][1]

print(count)