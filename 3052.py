n_list = []

for i in range(0,10):
    a = int(input())
    b = a%42
    n_list.append(b)
    
c = set(n_list)
print(len(c))
        