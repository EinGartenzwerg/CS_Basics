# loosely based on @EinGartenzwerg s Java implementation of the knapsackproblem
# translation into python by @EinGartenzwerg
# alterations by @EinGartenzwerg

# def hike(sizes, values, size):
#     return wheelchair(sizes, values, size, len(values) - 1);
#
#
# def wheelchair(sizes, values, freeSpace, next):
#     if next < 0:
#         return 0
#
#     if sizes[next] > freeSpace:
#         return wheelchair(sizes, values, freeSpace, next - 1)
#     else:
#         return max(wheelchair(sizes, values, freeSpace - sizes[next], next - 1) + values[next],
#                    wheelchair(sizes, values, freeSpace, next - 1))
#
# if __name__ == '__main__':
#     # test main
#     sizes = [2, 3, 2, 2]
#     values = [1, 900, 2, 2]
#     capacity = 6
#     print(hike(sizes, values, capacity))

def hike(sizes, values, size):
    return wheelchair(sizes, values, size, len(values) - 1)


def wheelchair(sizes, values, freeSpace, next):
    if next < 0:
        orderr = [0] * len(values)

        return orderr, 0

    if sizes[next] > freeSpace:
        return wheelchair(sizes, values, freeSpace, next - 1)
    else:
        ret_l1 = wheelchair(sizes, values, freeSpace - sizes[next], next)

        order1 = ret_l1[0]
        val1 = ret_l1[1] + values[next]

        ret_li2 = wheelchair(sizes, values, freeSpace, next - 1)
        order2 = ret_li2[0]
        val2 = ret_li2[1]

        if val1 >= val2:
            order1[next] = order1[next] + 1
            return order1, val1
        else:
            return order2, val2


if __name__ == '__main__':
    # test main
    sizes = [215, 275, 335, 355, 420, 580]
    values = [1] * 6

    capacity = 1505
    value, order = hike(sizes, values, capacity)
    print(value)
    print(order)
