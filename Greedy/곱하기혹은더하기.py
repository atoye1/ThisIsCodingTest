'''
1. 앞, 뒤의 수가 뭔지에 따라서 연산이 달라진다.
2. 만약 앞의 숫자나 뒤의 숫자가 0이면 더하기.
3. 만약 앞의 숫자나 뒤의 숫자가 1이면 더하기.
4. 이외의 경우에는 곱하기를 한다.
'''
n = list(map(int, list(input())))
answer = n[0]  # 첫 번째 수는 연산없이 그대로 대입가능하다.
for i in n[1:]:
    if answer == 0 or answer == 1:
        answer += i
    elif i == 0 or i == 1:
        answer += i
    else:
        answer *= 1

print(answer)
