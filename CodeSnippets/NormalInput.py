import sys

# 일반적인 리스트로 입력받기
input_list = list(map(int, input().split()))
print(sorted(input_list))

# 개수가 정해져 있는 입력의 경우
a, b, c = map(int, input().split())
print(a, b, c)

# 빠르게 입력받기
input_string = sys.stdin.readline().rstrip()
print(list(map(int, input_string.split())))
