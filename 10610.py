N = list(map(int,input()))
N.sort(reverse=True)
sum = 0

if 0 not in N:
    print('-1')
else:
    for i in N:
        sum += i
    if sum % 3 != 0:
        print('-1')
    else:
        print(''.join(map(str,N)))