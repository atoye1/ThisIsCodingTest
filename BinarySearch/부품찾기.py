from bisect import bisect_left
import sys
n = int(sys.stdin.readline().rstrip())
stored = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
asked = list(map(int, sys.stdin.readline().rstrip().split()))
stored.sort()
asked.sort()


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for elem in asked:
    if binary_search(stored, elem):
        print('yes')
    else:
        print('no')
