# BOJ 1439

S = input()
is_first0, is_first1 = True, True
count0, count1 = 0, 0

for i in range(len(S)):
    if S[i] == '0':
        if is_first0:
            count0 += 1
            is_first0 = False
            is_first1 = True
    else:
        if is_first1:
            count1 += 1
            is_first1 = False
            is_first0 = True

print(min(count0, count1))
