count = 0
count2 = 0


def binary_search(arr, target, start, end):
    global count
    count += 1
    print('binary search called', count)
    if start > end:
        return False
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)


def binary_search_loop(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        global count2
        count2 += 1
        print('binary search loop called', count2)
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


a = list(range(100_000))
print(binary_search(a, 1, 0, len(a) - 1))

a = list(range(100_000))
print(binary_search_loop(a, 1))
