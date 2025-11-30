import sys

n, k = map(int, sys.stdin.readline().split())
money = []
count = 0

for i in range(n):
    a = int(sys.stdin.readline())
    money.append(a)

re = money[::-1]

for i in re:
    if i <= k: 
        use = k // i
        count += use
        k %= i

print(count)