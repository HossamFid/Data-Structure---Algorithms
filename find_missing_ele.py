# 2 arrays - second is formed by shuffling the elements of the first array
# then deleting  a random element from second array then find out which element is missing out



def finder(lst1, lst2):

    lst1.sort()
    lst2.sort()

    for num1 , num2 in zip(lst1, lst2):
        if num1 != num2 :
            return num1

        return lst1[-1]



print(finder([1,2,3,4],[2,3,4]))


import collections

def finder2(lst1,lst2):

    dic = collections.defaultdict(int)

    for num in lst2:
        dic[num] +=1

    for num in lst1:
        if dic[num] == 0:
            return num

        else :
            dic[num] -= 1

print(finder2([1,2,3,4],[2,3,4]))



# using XOR

def finder3(lst1,lst2):

    result = 0
    for num in lst1+lst2 :
        result ^= num
        print(result)

    return result

print(finder2([1,2,3,4],[2,3,4]))
