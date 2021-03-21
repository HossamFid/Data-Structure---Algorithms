

def quick_sort(array):

    # check the len of the array

    if len(array) <= 1 :
        return array

    else :

        # define our pivot point

        pivot = array.pop()

        # make 2 lists greater than and lower than pivot

        greater_list = list()
        lower_list = list()

        # iterate over the array using pivot point to define the above 2 lists

        for item in array :
            if item > pivot:
                greater_list.append(item)
            else :
                lower_list.append(item)

        # now apply this to every sub list that we create (lower & greate)
        return quick_sort(lower_list) + [pivot] + quick_sort(greater_list)


print(quick_sort([1,5,7,6,7,2,4,1]))
