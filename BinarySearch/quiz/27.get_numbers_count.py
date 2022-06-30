def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)

    if a is None:
        return 0

    b = last(array, x, 0, n-1)
    print(a, b)

    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif target > array[mid]:
        return first(array, target, mid + 1, end)
    else:
        return first(array, target, start, mid - 1)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 현재 위치가 끝이거나, 내 오른쪽 인덱스의 값이 찾는 값보다 큰 경우 리턴
    if (mid == len(array) - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif target >= array[mid]:
        return last(array, target, mid + 1, end)
    else:
        return last(array, target, start, mid - 1)


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)
