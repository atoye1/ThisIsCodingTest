import random

# n = int(input())
# mans = list(map(int, input().split()))


def my_solution(n, mans):
    mans.sort(reverse=True)

    group_counts = []

    for idx in range(n):
        group_count = 0
        while True:
            if idx >= n:
                break
            group_size = mans[idx]
            if idx + group_size > n:
                break
            else:
                group_count += 1
                idx = idx + group_size
        group_counts.append(group_count)
    return max(group_counts)


def book_solution(n, mans):
    mans.sort()
    result = 0
    count = 0

    for i in mans:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result


for _ in range(10):
    n = 20
    mans = [random.randint(1, 20) for _ in range(20)]
    print(mans)
    assert my_solution(n, mans) == book_solution(n, mans)
