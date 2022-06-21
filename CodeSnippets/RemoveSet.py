def remove_list(my_list, remove_set):
    return [i for i in my_list if i not in remove_set]


my_list = [1, 2, 3, 4, 1, 2, 3, 4]
remove_set = {2, 3}

print(remove_list(my_list, remove_set))
