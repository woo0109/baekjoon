import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int, input().split()))
m = int(input())
weight = list(map(int, input().split()))

limit.sort(reverse=True)
weight.sort(reverse=True)

if weight[0] > limit[0]:
    print("-1")
    exit()

check = [False] * m
count = 0
minute = 0

positions = [0] * n 

while count < m:
    minute += 1
    for i in range(n): 
        while positions[i] < m:
            if not check[positions[i]] and limit[i] >= weight[positions[i]]:
                check[positions[i]] = True
                count += 1
                break
            positions[i] += 1

print(minute)