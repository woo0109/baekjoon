n, k = map(int,input().split())
ball =k*(k+1)//2

if n < ball:
    print(-1)
elif (n - ball) % k == 0:
    print(k-1)
else:
    print(k)