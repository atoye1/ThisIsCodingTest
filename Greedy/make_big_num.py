def solution(number, k):
    num_list = list(map(int, list(number)))

    while k > 0:
        new_list = [i for i in num_list]
        is_removed = False

        for i in range(len(num_list) - 1):
            if num_list[i] < num_list[i + 1]:
                new_list.remove(num_list[i])
                k -= 1
                is_removed = True
                if k == 0:
                    break
        if not is_removed:
            k -= 1
            new_list = new_list[0:-1]
        num_list = new_list
    answer = ''.join(map(str, num_list))
    return answer


print(solution("4177252841", 4))
