N, M = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
print(game_map)
print(x, y, d)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # north, east, south, west

game_map[x][y] = 2
visited_count = 1
blocked_count = 0

while True:
    print(x, y)
    d = (d + 3) % 4  # 회전하기
    next_x, next_y = x + directions[d][0], y + directions[d][1]
    next_pos = game_map[next_x][next_y]
    if next_pos == 0 or next_pos == 2:
        x, y = next_x, next_y
        game_map[x][y] = 2
        blocked_count = 0
        visited_count += 1
    # 0이 아니면 방향을 바꿔서 재탐색 한다.
    # 모든 방향을 탐색해본 후, 방향을 유지하고 뒤로 간다.
    # 뒤로 갈 공간도 없으면 종료한다.
    elif blocked_count == 4:
        next_x, next_y = x - directions[d][0], y - directions[d][1]
        next_pos = game_map[next_x][next_y]
        if next_pos == 1:
            break
        else:
            x, y = next_x, next_y
            blocked_count = 0
    else:
        blocked_count += 1
        continue
print(visited_count)
for i in game_map:
    for j in i:
        print(j, end=' ')
    print()
