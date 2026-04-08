n, k = input().split()
count = 0
n_list = list(n)

def swap(a, b):
    state = a
    a = b
    b = state

    return a, b

current = [n]

for _ in range(int(k)):
    num = set()

    for s in current:
        s_list = list(s)

        for i in range(len(n_list) - 1):
            for j in range(i + 1, len(n_list)):
                s_list[i], s_list[j] = swap(s_list[i], s_list[j])

                if s_list[0] == '0':
                    continue

                num.add("".join(s_list))

    if not num:
        print('-1')
        exit()

    current = num

print(max(current))