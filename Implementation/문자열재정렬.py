print(dir('string'))
s = list(input())
s.sort()
total = 0
for c in s:
    if c.isdigit():
        total += int(c)
    else:
        print(c, end='')
print(total)
