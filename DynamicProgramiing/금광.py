'''
2차원 배열을 해석하는 방법이 선행되어야 한다.
row, col로 표현하는 방법과 일반적인 (x, y)방식으로 표현하는게 다름을 유의해야 한다.
row는 세로인덱스를 말하며, col은 가로 인덱스를 말한다.
'''

# 첫 번째 열부터 가능하므로 가능한 최댓값을 기록하내가면서 선택하는 것
# 이거 스트링편집거리문제랑 유사한데, 최댓값을 찾으면 되는건가?
'''
1,1 1,2 1,3 1,4
2,1 2,2 2,3 2,4
3,1 3,2 3,3 3,4
'''
case_count = int(input())
cases = []
for i in range(case_count):
    n, m = map(int, input().split())
    map = []
    for row in range(n):
        rows = []:
        for col in range(m):
            rows.append(int(input()))
    cases.append()

# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우 만약 i == 0이면 올 수 없으니깐 최솟값인 0으로 설정한다.
            left_up = 0 if i == 0 else dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우 만약 i == n - 1 이면 올 수 없으므로 0으로 설정한다.
            left_down = 0 if i == n - 1 else dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
