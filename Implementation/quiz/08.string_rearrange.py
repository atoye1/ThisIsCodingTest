s = list(input())
s.sort()
answer = ''
num = 0
for c in s:
    if c.isalpha():
        answer += c
    else:
        num += int(c)
print(answer + str(num))
