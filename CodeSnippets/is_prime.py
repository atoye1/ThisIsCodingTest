# 소수를 판별하는 함수입니다.
# 소수는 2이상의 수 중에 1과 자기자신으로만 나눠지는 수를 의미합니다.
import math


def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# 에라토스테네스의 체 방법을 활용한 소수 찾기
# 여러개의 소수를 찾을 때 활용하는 방법으로 N보다 작거나 같은 모든 수를 찾을 때 사용하는 방법이다.
def is_prime_sieve(n):
    arr = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            j = 2  # i를 제외한 i의 모든 배수를 제거해줘야 하므로 j = 2로 초기화 하고, 1씩 증가시키면서 i의 모든 배수들을 제거해준다
            while i * j <= n:
                arr[i * j] = False
                j += 1
    return arr  # True, False로 거를 수 있는 배열을 반환한다.


num = 101
sieve = is_prime_sieve(num)
for i in range(num + 1):
    if sieve[i]:
        print(i, end=' ')
