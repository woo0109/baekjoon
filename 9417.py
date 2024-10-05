import sys
import math

N = int(sys.stdin.readline())

for i in range(N):
    arr = list((map(int, sys.stdin.readline().split())))
    sm = []
    smm = []

    for j in arr:
        for k in range(1, int(math.sqrt(j))+1):
            if j % k == 0:
                sm.append(k)
                sm.append(j//k)

    for j in sm:
        if sm.count(j) >=2:
            smm.append(j)
    smm = set(smm)
    print(max(smm))