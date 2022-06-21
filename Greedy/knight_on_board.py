coord = input()
position = (ord(coord[0]) - ord('a') + 1, int(coord[1]))
print(position)

count = 0
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1)]

for move in moves:
    if move[0] + position[0] >= 1 and move[0] + position[0] <= 8:
        if move[1] + position[1] >= 1 and move[1] + position[1] <= 8:
            count += 1

print(count)
