import random


def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1
    print("count array is : ", end=' ')
    print(count)

    arr_idx = 0
    # 인덱스와, 배열에 저장된 값이 헷갈려서 시간이 오래 걸렸다.
    # 인덱스와 값을 확실히 구분해서 활용하자.
    # 버그 발생시 어떤 변수가 인덱스고, 어떤 변수가 값인지 잘 파악하면 좋다.
    for i in range(len(count)):
        if count[i] == 0:
            continue
        for j in range(count[i]):
            arr[arr_idx] = i
            arr_idx += 1
    print("sorted array is : ", end=' ')
    print(arr)
    return arr


if __name__ == "__main__":
    arr = [random.randint(0, 9) for _ in range(15)]
    print("original array is : ", end=' ')
    print(arr)
    assert counting_sort(arr) == sorted(arr)
