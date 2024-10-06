P = [[0] for _ in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1

for i in range(4, 101):
    P[i] = P[i-2] + P[i-3]
    
t = int(input())
for i in range(t):
    n = int(input())
    print(P[n])

# import sys
# input = sys.stdin.readline

# def func(x):    
#     if x == 1 or x == 2 or x == 3:
#         return 1
#     else:
#         return func(x-2) + func(x-3)
    
# t = int(input())

# for i in range(t):
#     n = int(input())
#     print(func(n))