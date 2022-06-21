
N, M = map(int, input().split())
A, B, d = map(int, input().split())

game_map = [[i for i in map(int, input().split())] for _ in range(N)]
directions = [0, 1, 2, 3]
d_change_count = 0
move_count = 1


def moveable(A, B):
    if game_map[A][B] == 0:
        return True
    return False


game_map[A][B] = 2

while True:

    if d_change_count == 4:
        # direction 별로 구성해서 뒤로가는 로직 구현하기

        break

    d = (d - 1) % 3  # 매번 시작할 때마다 왼쪽으로 방향을 전환한다.
    if d == 0:
        if moveable(A - 1, B):  # upward
            move_count += 1
            game_map[A - 1][B] = 2
            A -= 1
        else:
            d_change_count += 1

    elif d == 1:  # rightward
        if moveable(A, B + 1):
            move_count += 1
            game_map[A][B + 1] = 2
            B += 1
        else:
            d_change_count += 1
    elif d == 2:  # downward
        if moveable(A + 1, B):
            move_count += 1
            game_map[A + 1][B] = 2
            A += 1
        else:
            d_change_count += 1
    elif d == 3:
        if moveable(A, B - 1):
            move_count += 1
            game_map[A][B - 1] = 2
            B -= 1
        else:
            d_change_count += 1

print(move_count)
