'''
(최솟값)선택정렬은
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸는 것
정렬 자체로는 최적화 할 수 있는 부분이 작으므로 비효율적이다.
내장 sort()함수와 비교해서도 비효율적인 정렬이다.
하지만 선택정렬의 로직은 코딩테스트에서 많이 사용되는 최솟값는데 사용되므로 익숙해질 필요가 있다.
'''

target = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(target):
    # 첫 번째 원소부터 루프를 돈다.
    for i in range(len(target)):
        min_idx = i
        # 자신까지를 제외한 배열에서 최솟값을 찾는다.
        for j in range(i + 1, len(target)):
            if target[min_idx] > target[j]:
                min_idx = j
        # 찾은 최솟값을 스왑해준다.
        target[i], target[min_idx] = target[min_idx], target[i]

    return target


print(selection_sort(target))
