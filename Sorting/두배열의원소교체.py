N, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort(reverse=True)
arr2.sort()
answer = 0
while K > 0:
    arr1.pop()
    answer += arr2.pop()
    K -= 1
answer += sum(arr1)
print(answer)
