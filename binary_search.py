



# must be sorted

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) -1   # cuz it starts with zeros indexing

    while begin_index <= end_index :

        mid_point = begin_index + (end_index - begin_index) // 2  # index         start + (end - start ) // 2
        mid_value = sequence[mid_point]   # value

        if mid_value  == item :
            return mid_point  # index

        elif item < mid_value :
            end_index = mid_point -1   # left portion

        else :   # item > mid_value
            begin_index = mid_point +1    # right portion

    return None # not found

print(binary_search([1,2,3,4,5,6], 2))
