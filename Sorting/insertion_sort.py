import random
arr = [random.randint(1, 100) for _ in range(20)]


def insertion_sort(arr):
    sorted_arr = arr[:1]
    unsorted_arr = arr[1:]
    while unsorted_arr:
        elem = unsorted_arr.pop()
        idx = len(sorted_arr)
        for i in range(len(sorted_arr)):
            if sorted_arr[i] >= elem:
                idx = i
                break
        sorted_arr.insert(idx, elem)
        print(sorted_arr)
        print(unsorted_arr)
    return sorted_arr


def insertion_sort2(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] <= arr[j]:
                arr.insert(j, arr.pop(i))
                continue
    return arr


result_arr = insertion_sort(arr)
result_arr2 = insertion_sort2(arr)
print(result_arr)
print(result_arr2)
print(sorted(arr))

assert result_arr == sorted(arr)
assert result_arr2 == sorted(arr)
