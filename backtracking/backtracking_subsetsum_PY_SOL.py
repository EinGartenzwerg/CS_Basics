# code loosely based on https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
# with a lot of changes by @EinGartenzwerg
import numpy as np


def partition_helper(elements, taken,
                     subsetsize, parts, size, curIdx, limitIdx, subsets):
    if np.sum(subsets[curIdx]) == subsetsize:

        # if size - 1 subsets are possible, then the last subset is also possible.
        if curIdx == parts - 2:
            for idx, elem in enumerate(taken):
                if not elem:
                    subsets[parts - 1].append(elements[idx])
            return subsets

        return partition_helper(elements, taken,
                                subsetsize, parts, size, curIdx + 1, size - 1, subsets)

    # start from limitIdx and include
    # elements into current partition
    for i in range(limitIdx, -1, -1):

        if taken[i]:
            continue

        # free space in the partition
        if (np.sum(subsets[curIdx]) + elements[i]) <= subsetsize:

            # Backtracking: Put in
            taken[i] = True
            subsets[curIdx].append(elements[i])

            if partition_helper(elements, taken, subsetsize, parts, size, curIdx, i - 1, subsets):
                return subsets

            # Backtracking: if not solution - take out
            # @Sebastian: Go over standard Backtracking schema
            taken[i] = False
            subsets[curIdx].remove(elements[i])
    return False


# returns true if partitioning possible, else False
def partition(elements, parts, size):

    # array is partition
    if size == 1:
        return elements

    # check if partitioning is possible: not more partitions than elements, elements distributable to partitions
    summe = np.sum(elements)
    if parts < size | summe % size != 0:
        return False

    subsets = [[] for i in range(size)]
    print(subsets)
    # mark all elements as not taken
    taken = [False] * parts

    # init: last element
    taken[parts - 1] = True
    subsets[0].append(elements[parts - 1])
    print(subsets)

    return partition_helper(elements, taken,
                            summe // size, size, parts, 0, parts - 1, subsets)


if __name__ == '__main__':

    test_arr = [4, 5, 96, 90, 5, 100]
    parts = len(test_arr)
    example_size = 3
    res = partition(test_arr, parts, example_size)

    # @Sebastian: explain, why this condition works (no boolean)
    if res:
        print("Partitioning finished:")
        print(res)
    else:
        print("Partitioning not possible.")

    # @Sebastian: for minimal partition:
    # for i in range(parts):
    #     res2 = partition(test_arr, parts, i)
    #     if res2:
    #         print("Partitioning finished:")
    #         print(res2)
    #     else:
    #         print("Partitioning not possible.")
