'''
수열을 내림차순으로 정렬하는 문제
'''
n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort(reverse=True)
print(' '.join(map(str, numbers)))
