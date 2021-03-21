


def bubble(sequence):

    seq_len = len(sequence) -1
    is_sorted = False 


    while not is_sorted:

        is_sorted = True 

        for i in range(0 , seq_len):
            if sequence[i] > sequence[i+1]:   # once this condition is not true is_sorted will remain True and will break our loop
                is_sorted = False
                sequence[i] , sequence[i+1] = sequence[i+1] , sequence[i]
    return sequence

print(bubble([2,4,5,7,1,10]))
                


