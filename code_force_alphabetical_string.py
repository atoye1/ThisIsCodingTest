def solution(s):
    if not s:
        return False

    if len(s) == 1:
        if s[0] == 'a':
            return True
        else:
            return False
    first = s[0]
    last = s[-1]
    print(f"first {first}, last {last}")
    if first == last:
        return False
    elif first > last:
        target = s.pop(0)
        print("target :", target)
        if ord(target) - ord(s[0]) == 1:
            solution(s)
        elif ord(target) - ord(s[-1]) == 1:
            solution(s)
        else:
            return False
    else:
        target = s.pop(-1)
        print("target :", target)
        if ord(target) - ord(s[0]) == 1:
            solution(s)
        elif ord(target) - ord(s[-1]) == 1:
            solution(s)
        else:
            return False


n = int(input())
for _ in range(n):
    input_string = list(input())
    print(input_string)
    if solution(input_string):
        print('yes')
    else:
        print('no')
