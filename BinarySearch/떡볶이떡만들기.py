count, length = map(int, input().split())
lines = list(map(int, input().split()))
total = sum(lines)
max_line = max(lines)

'''
이진탐색의 시작점은 1인데, 1만큼 잘랐을 경우 왠만하면 가능할거거든
일단 처음에 sum을 구한다.
start부터 end의 범위까지 정렬되어 있으므로 이진탐색한다.
탐색의 종료조건은 어떻게 되는가?
'''
answer = -1
start = 1
end = max_line - 1
while start <= end:
    # mid가 자르는 길이다.
    mid = (start + end) // 2
    # mid로 잘랐을때 0이거나 0보다 작은 line은 토탈 계산에서 제외해야한다.
    new_total = sum([line - mid for line in lines if line - mid > 0])
    print(mid, new_total)
    # 만약 잘라낸 후의 길이가 손님이 원하는 길이가 아니면 더 적게 자르는쪽으로 탐색
    if new_total < length:
        end = mid - 1
    # 만약 손님이 원하는 길이 이상으로 자르는 것을 성공했으면
    # 최적화를 위해 더 많이 잘라도 되는지 탐색해봐야 한다.
    else:
        answer = mid
        start = mid + 1
print(answer)
