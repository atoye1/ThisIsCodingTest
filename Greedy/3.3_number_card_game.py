row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(sorted(list(map(int, input().split())))[0])
print(max(matrix))
