n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])
arr.sort()

area = 0
height = 0

for i in arr:
    