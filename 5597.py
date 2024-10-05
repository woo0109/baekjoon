n_list = [0]*30
for i in range(0,28):
    a = int(input())
    n_list[a-1] = a
for i in range(0,30):
    if n_list[i] == 0:
        print(i)