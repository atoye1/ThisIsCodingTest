def binary_search_recursive(arr, start, end, value):
    if start > end:
        return None
    mid = (end - start)//2
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return binary_search_recursive(arr, start, mid - 1, value)
    else:
        return binary_search_recursive(arr, mid + 1, end, value)


def binary_search_loop(target, List):
    """
        target에서 찾은 인덱스를 반환함
    """
    left = 0
    right = len(List) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == List[mid]:
            return mid
        elif target < List[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None
