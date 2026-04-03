import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int,input().split()))
m = int(input())
weight = list(map(int, input().split()))
minute = 0

limit.sort(key=lambda x : -x)
weight.sort(key=lambda x :-x)
check = [False] * m

if weight[0] > limit[0]:
    print("-1")
    exit()

while weight:
    minute += 1

    for l in limit:
        for j in range(len(weight)):
            if l >= weight[j] and check[j] != True:
                check[j] = True
                break

print(minute)            