def eat(idx, food_times):
    # 현재 먹어야 할 인덱스가 idx일 때 다음 먹어야 할 인덱스를 반환하는 함수
    initial_idx = idx
    while food_times[idx] == 0:
        idx += 1
        if idx == len(food_times):
            idx = 0
        if idx == initial_idx:
            return -1
    food_times[idx] -= 1
    next_idx = idx + 1
    if next_idx == len(food_times):
        next_idx = 0
    return next_idx


def solution(food_times, k):
    time = 0
    idx = 0

    while True:
        idx = eat(idx, food_times)
        time += 1
        if time == k:
            print(idx + 1)


food_times = [3, 1, 2]
k = 5

solution(food_times, k)
