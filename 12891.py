s, p = map(int,input().split())
pw = input()
a, c, g, t = map(int, input().split())
answer = 0

count = {'A' : 0, 'G' : 0, 'C' : 0, 'T' : 0}

for i in range(p):
    count[pw[i]] += 1

if count['A'] >= a and count['C'] >= c and count['G'] >= g and count['T'] >= t:
    answer += 1

for i in range(p, s):
    count[pw[i-p]] -= 1
    count[pw[i]] += 1

    if count['A'] >= a and count['C'] >= c and count['G'] >= g and count['T'] >= t:
        answer += 1

print(answer)