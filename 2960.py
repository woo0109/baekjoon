n, k = map(int,input().split())
list = [0] * (n+1)
cnt = 0

for i in range(2,n+1):
    if list[i] == 0:
        for  j in range(i, n+1, i):
            if list[j] == 0:
                list[j] = 1
                cnt+=1
                
                if cnt == k:
                    print(j)