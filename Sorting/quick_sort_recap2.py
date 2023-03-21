import random


def qsort_py(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = 0
    mid_arr = []
    left_arr = []
    right_arr = []
    for i in arr:
        if i == arr[pivot_idx]:
            mid_arr.append(i)
        elif i < arr[pivot_idx]:
            left_arr.append(i)
        else:
            right_arr.append(i)
    return qsort_py(left_arr) + mid_arr + qsort_py(right_arr)


target = [random.randint(1, 100) for _ in range(10)]
print(target)
print(qsort_py(target))


def qsort_while(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
    qsort_while(arr, start, right - 1)
    qsort_while(arr, right + 1, end)

    return arr


target = [random.randint(1, 100) for _ in range(10)]
print(target)
print(qsort_while(target, 0, len(target) - 1))
print(target)
