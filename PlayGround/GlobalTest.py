array = [1, 2, 3, 4]


def func():
    array.append(5)  # 함수 바깥의 array를 참조하여 변경시킨다.


func()
print(array)
