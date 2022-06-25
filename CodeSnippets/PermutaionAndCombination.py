from itertools import permutations as perm
from itertools import combinations as combi
# 순열과 조합 활용 예시

my_list = ['a', 'b', 'c']
print(list(combi(my_list, 2)))  # 순서와 상관없이 현재 iterable에서 두 수를 뽑는다.
print(list(perm(my_list, 2)))  # 순서와 상관있게 현재 iterable에서 두 수를 뽑는다.
