import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

A_transpose = A.T  # 전치행렬을 구하는 방법

print(A_transpose)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


def diagonal_flip(matrix):
    return [list(row) for row in zip(*matrix)][::-1]


print(diagonal_flip(A))
n = 3
new = [[0] * 3 for _ in range(3)]
new_r = [[0] * 3 for _ in range(3)]

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(new)
for i in range(n):
    for j in range(n):
        new[i][j] = arr[j][n - i - 1]
        new_r[j][n - i - 1] = arr[i][j]
print('left', new)
print('right', new_r)


def roate_left(arr):
    n = len(arr)
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # arr[i][j] = new[n - j - 1][i]
            new[i][j] = arr[j][n - 1 - i]
    return new


arr = [[(0, 0), (0, 1), (0, 2)],
       [(1, 0), (1, 1), (1, 2)],
       [(2, 0), (2, 1), (2, 2)]]
print('roate left', roate_left(arr))


def rotate_key_90(key):
    n = len(key)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = key[n - j - 1][i]
    return rotated


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print('roate right', rotate_key_90(arr))
