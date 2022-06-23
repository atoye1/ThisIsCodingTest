import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    print(selection_sort(arr))
    print(sorted(arr))
    assert selection_sort(arr) == sorted(arr)
