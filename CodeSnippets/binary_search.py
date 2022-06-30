def binary_search_recursive(arr, value, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        # 재귀적으로 호출하는 결과를 return해줘야 하는 것을 잊지말지
        return binary_search_recursive(arr, value, start, mid - 1)
    else:
        return binary_search_recursive(arr, value, mid + 1, end)


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
