'''
1. 0과 1로 이루어진 문자열을 뒤집어서 모두 같게 만들어야한다.
2. 0을 뒤집는 경우와 1을 뒤집는 경우를 카운트해서 작은 경우를 반환하면 된다.
3. 연속된 동일 숫자는 한번에 뒤집을 수 있으므로 연속된 경우 카운트를 갱신하지않고
    계속 뽑아줘야한다.
'''
n = list(input())
last = False
counter = {'0': 0, '1': 0}
while n:
    curr = n.pop()
    if curr != last:
        counter[curr] += 1
        last = curr
print(min(counter['0'], counter['1']))
