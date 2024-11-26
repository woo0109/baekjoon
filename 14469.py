n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort()
time = 0

for i in range(n):
    if time > arr[i][0]:
        time += arr[i][1]
    else:
        time = arr[i][0] + arr[i][1]
    
print(time)