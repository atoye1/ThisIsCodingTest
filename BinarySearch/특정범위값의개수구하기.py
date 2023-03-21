from bisect import bisect_left, bisect_right


def get_count_by_range(a, left_val, right_val):
    l_idx = bisect_left(a, left_val)
    r_idx = bisect_right(a, right_val)
    return r_idx - l_idx
