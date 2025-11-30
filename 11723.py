import sys

m = int(sys.stdin.readline())
l = []

for i in range(m):
    ip = sys.stdin.readline().split()
    a = ip[0]

    if a == 'add':
        b = int(ip[1])
        if b not in l:
            l.append(b)

    elif a == 'remove':
        b = int(ip[1])
        if b in l:
            l.remove(b)

    elif a == 'check':
        b = int(ip[1])
        if b in l:
            print('1')
        else:
            print('0')

    elif a == 'toggle':
        b = int(ip[1])
        if b in l:
            l.remove(b)
        else:
            l.append(b)
            
    elif a == 'all':
        l.clear()
        for i in range(1,21):
            l.append(i)

    elif a == 'empty':
        l.clear()