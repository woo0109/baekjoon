X = int(input())
N = int(input())
sum = 0

for i in range(0,N):
    a, b = map(int, input().split())
    sum = a*b + sum
if X == sum:
    print("Yes")
else:
    print("No")