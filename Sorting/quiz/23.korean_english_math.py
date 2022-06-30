import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    name, kor, eng, math = input().split()
    idv_data = [name, int(kor), int(eng), int(math)]
    data.append(idv_data)
data.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])
for stu in data:
    print(stu[0])
