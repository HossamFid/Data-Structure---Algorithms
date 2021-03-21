


def binary(sequence, item):
    position = -1
    i = 0

    while i < len(sequence):
        if sequence[i]  == item :
            position = i
            return f'found at {position} index '
            i += 1

    return False



print(binary([1,5,3,4,8,9,2], 2))
