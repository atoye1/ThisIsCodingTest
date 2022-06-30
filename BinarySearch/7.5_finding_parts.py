n = int(input())
store = list(map(int, input().split()))
store.sort()

m = int(input())
order = list(map(int, input().split()))


def bin_search(arr, start, end, val):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return bin_search(arr, start, mid - 1, val)
    else:
        return bin_search(arr, mid + 1, end, val)


def bin_search_loop(arr, val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] >= val:
            end = mid - 1
        else:
            start = mid + 1
    return None


print(store)
print(order)
for i in order:
    if bin_search_loop(store, i) is not None:
        print("yes")
    else:
        print("no")
