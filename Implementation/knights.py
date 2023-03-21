current = input()
coord = [int(current[1]), ord(current[0]) - ord('a') + 1]
dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

count = 0

for i in range(8):
    nx = coord[0] + dx[i]
    ny = coord[1] + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1
print(count)
