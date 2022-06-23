N = int(input())
students = []
for _ in range(N):
    students.append((input().split()))

students.sort(key=lambda x: x[1])

for student in students:
    print(student[0], end=' ')
