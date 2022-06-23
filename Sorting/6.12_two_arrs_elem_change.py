N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(A)
print(B)

A.sort()
B.sort(reverse=True)
for i in range(K):
    # 값을 비교해서 A가 B보다 작을때만 원소를 교환한다.
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))
