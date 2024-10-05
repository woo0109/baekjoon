grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

sum = 0
total = 0

for i in range(20):
    n, g, s = input().split()
    if s != 'P':
        total += float(g)
        sum += float(g)*score[grade.index(s)]

print(sum/total)