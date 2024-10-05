a = int(input())
b = int(input())
sum = 0

for i in range(b):
    c, d = map(int,input().split())
    sum += c*d

if a == sum:
    print("Yes")
else:
    print("No")