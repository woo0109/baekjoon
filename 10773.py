n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

i = 0

while i < len(l):
    if l[i] == 0 and i > 0:
        l.pop(i)
        l.pop(i-1)
        i -= 1
    else:
        i += 1

print(sum(l))