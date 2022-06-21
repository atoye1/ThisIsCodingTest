def sortfunc(x):
    return x[1]


input_list = [('a', 10), ('b', 5), ('c', 1)]
print(sorted(input_list, key=sortfunc))
print(sorted(input_list, key=lambda x: x[1]))

list1 = [i for i in range(10)]
list2 = [i for i in range(10, 20)]
print(list1)
print(list2)

# list3 = list1 + list2 일때 람다식을 활용해라
print(list(map(lambda a, b: b-a, list1, list2)))
