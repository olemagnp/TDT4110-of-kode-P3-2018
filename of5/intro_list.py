
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [i for i in range(10)]

print(my_list)

my_list[-1] = 5

print(my_list)

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = "PARTALL"

print(my_list)


def half_list(l):
    return l[:len(l)//2]


my_list = half_list(my_list)

print(my_list)


def mid_list(l):
    return l[1:-1]


my_list = mid_list(my_list)

print(my_list)


def every_other(l):
    return l[::2]


print(every_other(my_list))