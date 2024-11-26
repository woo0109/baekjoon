n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n % 2 == 0:
    print(arr[int(n/2-1)])
else:
    print(arr[int((n+1)/2-1)])