t = int(input())

for i in range(t):
    n = int(input())
    a = n//25
    b = (n-a*25)//10
    c = (n-a*25-b*10)//5
    d = (n-a*25-b*10-c*5)
    print(a, b, c, d)