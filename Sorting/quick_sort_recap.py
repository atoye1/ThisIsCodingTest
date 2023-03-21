

def qsort_pythonic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    mid = [pivot]
    for i in arr[1:]:
        if i == pivot:
            mid.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    return qsort_pythonic(left) + mid + qsort_pythonic(right)


target = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('before', target)
print('after', qsort_pythonic(target))


def qsort_while(arr, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right >= start and arr[right] > arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    qsort_while(arr, start, right - 1)
    qsort_while(arr, right + 1, end)
    return arr


target = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('before', target)
qsort_while(target, 0, len(target) - 1)
print('after', target)
