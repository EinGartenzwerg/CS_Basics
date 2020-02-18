# there is a mistake in this implementation -> correct it!

def color(matrix, x, y, col):
    if x > len(matrix)-1 or y > len(matrix)-1 or x < 0 or y < 0:
        return
    if validate_n(matrix, x, y):
        if x < len(matrix) - 1:
            color(matrix, x + 1, y, 0)
        else:
            color(matrix, 0, y + 1, 0)
    else:
        matrix[x][y] = col
        color(matrix, x, y, col + 1)


def validate_n(matrix, x, y):
    c = matrix[x][y]
    if x > 0:
        if matrix[x - 1][y] == c:
            return False
    if y > 0:
        if matrix[x][y - 1] == c:
            return False
    if y < len(matrix) - 1:
        if matrix[x][y + 1] == c:
            return False
    if x < len(matrix) - 1:
        if matrix[x + 1][y] == c:
            return False
    return True


if __name__ == '__main__':
    n = 10
    matrix = [[x for x in range(n)] for i in range(n)]
    color(matrix, 0, 0, 0)
    print('\n'.join([''.join(['{:n}'.format(item) for item in row])
                     for row in matrix]))

