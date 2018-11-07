

def sum_of_list(lst):
    total = 0
    for el in lst:
        if isinstance(el, list):
            total += sum_of_list(el)
        else:
            total += el
    return total


print(sum_of_list([1, 3, [5, 3], [6, [4, 2]]]))
