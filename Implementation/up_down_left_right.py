num = int(input())
directions = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for move in directions:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue
    x, y = nx, ny
print(x, y)
