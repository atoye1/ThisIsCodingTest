N = int(input())
numbers = [int(input()) for _ in range(N)]

print(' '.join(map(str, sorted(numbers, reverse=True))))
