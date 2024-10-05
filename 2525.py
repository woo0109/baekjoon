A, B = map(int, input().split())
C = int(input())
a=int((B+C)/60)

if (B+C)%60==0:
    if A+a>=24:
        print(A+a-24, 0)
    else:
        print(A+a, 0)
elif (B+C)>60:
    if A+a>=24:
        print(A+a-24, (B+C)-60*a)
    else:
        print(A+a, (B+C)-60*a)
else:
    print(A, B+C)