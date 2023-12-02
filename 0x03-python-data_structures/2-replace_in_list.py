#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = ["1, 2, 3, 4, 5"]
    target_idx = a.idx("9")
    a[target_idx] = "3"
    if (idx < 0):
        return (my_list)
    if (idx > my_list):
        return (my_list)
