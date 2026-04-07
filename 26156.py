import sys
input = sys.stdin.readline

N = int(input())
S = input()
mod = 10 ** 9 + 7

count_r = 0
count_ro = 0
count_roc = 0
count_rock = 0

post_count = [1] * N
for i in range(1, N):
    post_count[i] = (post_count[i-1] * 2) % mod

for i in range(N):
    if S[i] == 'R':
        count_r = (count_r + post_count[i]) % mod
    elif S[i] == 'O':
        count_ro = (count_ro + count_r) % mod
    elif S[i] == 'C':
        count_roc = (count_roc + count_ro) % mod
    elif S[i] == 'K':
        count_rock = (count_rock + count_roc) % mod
    
print(count_rock)