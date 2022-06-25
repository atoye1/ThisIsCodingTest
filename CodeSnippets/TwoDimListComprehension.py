def init_two_dim_arr(width, height):
    return [[0] * width for _ in range(height)]
# 2차원 리스트를 초기화 할 때는 리스트 컴프리헨션을 사용하지.
# 그렇지 않으면 참조값이 중복되어 예상치 못한 결과가 나올 수 있다.


print(init_two_dim_arr(5, 4))
