# taken from https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# and slightly modified by @EinGartenzwerg
import numpy as np

# Function to print permutations of string
# This function takes three parameters:
# 1. List or String or similar
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, left, right):
    if left == right:
        print(a)
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permute(a, left + 1, right)
            a[left], a[i] = a[i], a[left]


def permute_return(a, left, right):
    if left == right:
        return a
    else:
        res = list()
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            for elem in permute_return(a, left + 1, right):
                res.append(elem)
            # @Sebastian: Erkläre, wieso das nicht funktioniert:
            # res.append(permute_return(a, left + 1, right))
            a[left], a[i] = a[i], a[left]
        return np.array(res).reshape((-1,3))


if __name__ == '__main__':

    INPUT = "ABC"

    print("STANDARD PERMUTATE: ")
    permute(list(INPUT), 0, len(INPUT) - 1)

    print("RETURNING PERMUTATE: ")
    print(permute_return(list(INPUT), 0, len(INPUT) - 1))

