'''
삽입정렬을 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하면서 구현한다.
선택정렬에 비해 구현 난이도가 높지만 일반적으로 더 효율적으로 동작한다.
일반적으로 2차시간에 동작하지만 이미 정렬되어 있는 최선의 경우에는 선형시간에 동작한다.

0. 0번 원소는 이미 정렬되어 있다고 가정한다.
1. 앞 쪽에 위치한 원소는 이미 정렬되어 있다고 가정한다.
2. 정렬된 데이터의 바로 옆에 위치한 원소를 순차적으로 앞쪽의 정렬된 데이터에 적절한 위치를 골라 넣는 것
3. 정렬된 데이터를 거꾸로 순회하면서 정렬할 원소와 단계적으로 스왑해나간다.
'''

target = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(target):
    for i in range(1, len(target)):  # i는 정렬할 대상을 의미한다.
        for j in range(i, 0, -1):  # j는 정렬할 대상원소부터 거슬러 올라가는 인덱스다.
            if target[j - 1] > target[j]:  # 만약 앞의 원소가 정렬할 대상원소보다 크면 스왑한다.
                target[j - 1], target[j] = target[j], target[j - 1]
            else:  # 만약 그렇지 않으면 j는 올바른 위치에 있는 것이므로 반복문을 탈출한다.
                break
    return target


print(insertion_sort(target))
