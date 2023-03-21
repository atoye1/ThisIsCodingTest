'''
1. 기준 테이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
2. 병합 정렬과 더불어 일반적인 상황에서 가장 많이 사용된다.
3. 쉽게 하려면 첫 번째 데이터를 기준으로 선택한다
4. 왼쪽의 데이터에서 피벗보다 큰 값을 선택하고, 오른쪽에선 작은 값을 선택한다.
5. 선택이 완료되면 둘을 스왑한다.
6. start와 end가 엇갈리면 왼쪽 배열의 마지막 값과 피벗을 스왑한다.
'''


def qsort_pythonic(target):
    if len(target) <= 1:
        return target
    pivot = target[0]

    left = [i for i in target if i < pivot]
    mid = [i for i in target if i == pivot]
    right = [i for i in target if i > pivot]
    return qsort_pythonic(left) + mid + qsort_pythonic(right)


def qsort_while(target, start, end):
    # 재귀에서 다루는 배열은 같은 배열임을 생각하자.
    # start, end 포인터만 변경해가면서 정렬을 수행하는 것이다.
    # 따라서 종료조건은 target의 length가 아니라 start와 end의 차이로 지정해야 한다.
    # 여기서 start와 end는 둘다 포함되는 범위이므로 range(start, end)와 다름을 생각하자.

    if start >= end:
        return
    pivot = (start + end) // 2  # 피벗도 인덱스로 지정한다. 인덱스와 실제 값을 헷갈리지말자
    target[pivot], target[start] = target[start], target[pivot]
    left = start + 1
    right = end
    # 두 개의 포인터가 교차하면 멈춰야 한다.
    while left <= right:
        # 왼쪽은 피벗보다 큰 숫자를 찾을 때 까지 계속 증가시켜준다.
        while left <= end and target[left] <= target[pivot]:
            left += 1
        # 오른쪽은 피벗보다 작은 숫자를 찾을 때 까지 증가시킨다.
        while right > start and target[right] >= target[pivot]:
            right -= 1
        # 만약 left와 right가 교차했다면 특수한 처리를 해줘야한다.
        # right가 멈춰 선 곳에 위치한 원소는 pivot보다 작거나 같은 원소이므로
        # 제일 첫 번째 원소인 pivot과 스위치해줘도 퀵정렬의 조건과 일치한다.
        if left > right:
            target[right], target[pivot] = target[pivot], target[right]
        # 교차하지 않았다면 left, right를 바꿔주면 된다.
        else:
            target[left], target[right] = target[right], target[left]
    # while문 안에서 피벗을 기준으로 한 정렬이 완료되었다.
    # 따라서 피벗을 제외한 양 옆의 배열을 대상으로 재귀적으로 퀵정렬을 호출해준다.
    # array 자체는 변화하지 않고 start, end인덱스 기준으로 퀵정렬을 수행할 구간을 지정하는 형식이므로
    # 이 형식에 맞게 호출해주어야한다.
    qsort_while(target, start, right - 1)
    qsort_while(target, right + 1, end)
    # partition 함수는 주어진 범위에서 피벗값을 기준으로 작은 값들과 큰 값들을 분리하는 역할을 수행하고, 피벗값의 위치를 반환합니다.


def partition(arr, low, high):
    # 피벗 인덱스를 중간값으로 설정합니다.
    pivot_index = (low + high) // 2
    # 피벗 인덱스의 값을 배열의 마지막 요소와 교환합니다.
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    # i는 작은 값들을 추적하는 인덱스로 사용됩니다.
    i = low - 1

    # low부터 high까지 반복하며 피벗값과 비교합니다.
    for j in range(low, high):
        if arr[j] <= pivot:
            # 작은 값들을 좌측에 유지하고 인덱스 i를 증가시킵니다.
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 마지막으로 피벗 값을 올바른 위치로 옮깁니다.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# quick_sort 함수는 재귀적으로 분할 정복 방식으로 정렬을 수행합니다.


def quick_sort(arr, low, high):
    if low < high:
        # 주어진 범위를 분할하여 피벗 인덱스를 얻습니다.
        pivot_index = partition(arr, low, high)
        # 피벗 인덱스를 기준으로 왼쪽 부분 배열을 정렬합니다.
        quick_sort(arr, low, pivot_index - 1)
        # 피벗 인덱스를 기준으로 오른쪽 부분 배열을 정렬합니다.
        quick_sort(arr, pivot_index + 1, high)


array = [3, 6, 8, 10, 1, 2, 1, -1]
print("Original array:", array)
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)
print('----------------')

array = [3, 3, 3, 1, 1, 2, 1, 0, -1, -1, 0]
print("WHILE Original array:", array)
qsort_while(array, 0, len(array) - 1)
print("WHILE Sorted array:", array)
print('----------------')

array = [3, 6, 8, 10, 1, 2, 1, -1]
print("Original array:", array)
print("Sorted array:", qsort_pythonic(array))
