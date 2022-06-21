s = input()
result = 0
for i in range(len(s) - 1):
    if int(s[i]) <= 1:
        sub_result = int(s[i]) + int(s[i+1])
    elif int(s[i+1]) <= 1:
        sub_result = int(s[i]) + int(s[i+1])
    else:
        sub_result = int(s[i]) * int(s[i+1])
    result += sub_result
