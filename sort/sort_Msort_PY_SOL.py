# generic solution from https://stackoverflow.com/questions/18761766/mergesort-with-python

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right)

if __name__ == '__main__':
    inputput = [1, 8, 4, 9, 3, 5]
    print(mergeSort(inputput))