

def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    reversed_part = reverse_list(lst[1:])
    return reversed_part + [lst[0]]


print(reverse_list([1, 2, 3, 4]))