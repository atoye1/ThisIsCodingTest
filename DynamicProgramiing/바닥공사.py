width = int(input())
height = 2
answer = 0

'''
1 * 2
2 * 1
2 * 2 
세가지의 타일이 있다.
width가 1인 타일을 채우는 경우
'''
memo = [0] * (width + 1)
memo[1] = 1
memo[2] = 3

for i in range(3, width + 1):
    memo[i] = (memo[i - 1] * 1) + (memo[i - 2] * 2)
print(memo[width])
