from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 정렬된 리스트에서 특정한 값이 속하는 범위를 구할 때 유용하다.


def count_by_range(a, left_value, right_value):
    # a 배열에서 값이 left이상, right이하인 원소의 개수를 반환하는 함수
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 3, 4))
