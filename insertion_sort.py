


def insertion_sort(sequence):

    indexing_length = range(1, len(sequence))

    for i in indexing_length:

        value_to_sort = sequence[i]
        print(value_to_sort)

        while sequence[i-1] > value_to_sort and i > 0 :

            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]  # swap
            print(sequence[i], sequence[i-1])
            print('#########')
            i= i-1

        
    return sequence


print(insertion_sort([3,5,4,7,9,8,2]))