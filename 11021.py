import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1,a+b))