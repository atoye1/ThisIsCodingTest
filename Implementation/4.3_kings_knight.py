init_coord = input()
col = ord(init_coord[0]) - ord('a')
row = int(init_coord[1]) - 1
init_coord = [row, col]

count = 0
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

for move in moves:
    dx = init_coord[0] + move[0]
    dy = init_coord[1] + move[1]
    if dx < 0 or dx > 7:
        continue
    if dy < 0 or dy > 7:
        continue
    count += 1

print(count)

"""
변수를 잘 설정하기만 해도 시행착오를 충분히 많이 줄일 수 있음.
"""
