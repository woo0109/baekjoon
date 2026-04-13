import sys
from math import comb
input = sys.stdin.readline

primes = [2, 3, 5, 7, 11, 13, 17]

a = int(input()) / 100.0
b = int(input()) / 100.0

a_probability = 0
b_probability = 0

for prime in primes:
    a_probability += comb(18, prime) * pow(a, prime) * pow((1 - a), (18 - prime))
    b_probability += comb(18, prime) * pow(a, prime) * pow((1 - b), (18 - prime))

answer = 1 - (1 - a_probability) * (1 - b_probability)
print(answer)