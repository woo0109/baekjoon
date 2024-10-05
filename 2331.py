a, p = map(int, input().split())
a_str = str(a)
list = []
list.append(a)

while True:
    tmp = 0

    for i in a_str:
        tmp += int(i) ** p

    if tmp in list:
        list = list[:list.index(tmp)]
        break
    else:
        list.append(tmp)
        a_str = str(tmp)

print(len(list))