N = int(input())

count = 0

"""
    따지는 경우의 수가 많지 않으므로, 브루트 포스로 풀어도 충분하다.
    
    파이썬의 경우 1초에 2천만번 정도 연산이 가능하다 생각하고 풀이하면 된다.
    
    다만 나는 좀더 최적화 하기 위해서 나머지 연산을 활용해서 3이 포함되는지 판정하였고, 경우에 따라 탐색하는 횟수를 줄이는
   는 방식으로 구현하였다
"""

for i in range(N + 1):
    if i % 10 == 3:
        count += 3600
        continue
    for j in range(60):
        if j // 10 == 3:
            count += 60
            continue
        elif j % 10 == 3:
            count += 60
            continue
        else:
            for k in range(60):
                if k // 10 == 3 or k % 10 == 3:
                    count += 1
                    print(i, j, k, sep=":")
print(count)
