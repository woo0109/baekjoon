a, b, c = map(int,input().split())

if b - a >= c - b:
    max = b - a - 1
else:
    max = c - b - 1

print(max)