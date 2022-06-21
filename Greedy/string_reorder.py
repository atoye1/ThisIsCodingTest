S = input()

result = []
count = 0

for c in S:
    if c.isalpha():
        result.append(c)
    else:
        count += int(c)
result.sort()
if count != 0:
    result.append(str(count))

print(''.join(result))
