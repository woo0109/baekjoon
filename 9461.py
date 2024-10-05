t = int(input())

def func(x):    
    if x == 1 or x == 2 or x == 3:
        return 1
    else:
        return func(x-2) + func(x-3)
    
for i in range(t):
    n = int(input())
    print(func(n))