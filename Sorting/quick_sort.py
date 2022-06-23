import random


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

    return arr


def quick_sort_pythonic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    mid_arr = [pivot]
    left_arr = []
    right_arr = []
    for i in arr[1:]:
        if i < pivot:
            left_arr.append(i)
        elif i > pivot:
            right_arr.append(i)
        else:
            mid_arr.append(i)
    return quick_sort_pythonic(left_arr) + mid_arr + quick_sort_pythonic(right_arr)


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    print(quick_sort(arr, 0, len(arr) - 1))
    print(quick_sort_pythonic(arr))
    print(sorted(arr))
    assert quick_sort_pythonic(arr) == sorted(arr)
