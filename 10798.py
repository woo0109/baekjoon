a, length = [], []
c =''

for i in range(5):
    A = input()
    a.append(A)
    length.append(len(A))

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            c += a[j][i]

print(c)