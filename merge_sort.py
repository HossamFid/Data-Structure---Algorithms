
def merge_sort(arr):

    # check for len of array > 1

    while len(arr) > 1 :

        # mid point to divide the array

        mid = len(arr) // 2

        # left array and right array

        left_array = arr[:mid]
        right_array = arr[mid:]

        # iterateve until reach to single element => recursive

        merge_sort(left_array)
        merge_sort(right_array)

        # now merge the left and right elements and store them into arr

        merge(left_array, right_array , arr)
