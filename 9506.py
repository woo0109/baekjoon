while True:
    n = int(input())
    list = []
    total = 0

    if n == -1:
        break

    for i in range(n):
        if n % (i+1) == 0:
            list.append(i+1)

    for i in range(len(list)-1):
        total+=list[i]

    if total == n:
        print("{} = 1".format(n),end='')
        for i in range(1, len(list)-1):
            print(" + {}".format(list[i]),end='')
        print("")
    else:
        print("{} is NOT perfect.".format(n))