n = int(input())
data = [input() for _ in range(n)]
data.sort(key=lambda x: int(x.split()[1]))
print(' '.join([i[0] for i in data]))
