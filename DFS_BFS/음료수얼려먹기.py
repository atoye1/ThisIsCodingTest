row, col = map(int, input().split())
board = [list(map(int, input())) for _ in range(row)]

# mark visited block with 2

count = 0


def dfs_stack(board, start_row, start_col):
    stack = [(start_row, start_col)]
    while stack:
        cur_row, cur_col = stack.pop()

        if cur_row < 0 or cur_row > len(board) - 1 or cur_col < 0 or cur_col > len(board[0]) - 1:
            continue
        elif board[cur_row][cur_col] != 0:
            continue
        elif board[cur_row][cur_col] == 0:
            board[cur_row][cur_col] = 2
            stack.append((cur_row + 1, cur_col))
            stack.append((cur_row, cur_col - 1))
            stack.append((cur_row - 1, cur_col))
            stack.append((cur_row, cur_col + 1))


for i in range(row):
    for j in range(col):
        if board[i][j] == 0:
            count += 1
            dfs_stack(board, i, j)

print(count)
