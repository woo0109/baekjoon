N = int(input())
arr = []
tip = 0

for i in range(N):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)

for i in range(N):
    if arr[i] - i < 0:
        continue
    tip += (arr[i] - i)

print(tip)