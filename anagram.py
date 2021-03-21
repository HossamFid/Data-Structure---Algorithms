# if 2 string are equal to each others once they are sorted so they are anagrams


'''def anagram(word1 , word2):
    # remove speaces and Caplizization
    word1 = word1.replace(' ','').lower()
    word2 = word1.replace(' ','').lower()

    # check for equality after sort them
    return True if  sorted(word1) == sorted(word2) else False'''


# check
#print(anagram('dog', 'god'))


# another solution
# counting every letter in first word and subtract the letters of second word from
# if the overall result is zero so its anagrams


def anagram2(word1, word2):
    # remove speaces and Caplizization
    word1 = word1.replace(' ','').lower()
    word2 = word1.replace(' ','').lower()

    # if thier length not equal so they arent
    print(word1)
    print(word2)
    if len(word1) != len(word2):
        return False

    # intializing counter as empty dict
    counter = {}

    # loop through the first word and add it the dict
    for i in word1 :
        if i in counter :
            counter[i] += 1
        else :
            counter[i] = 1
    print(counter)
    # loop over the second word and subtract it from counter
    for x in word2:
        if x in counter:
            counter[x] -= 1
        else :
            counter[x] = 1
    print(counter)
    # check for its all equal zeros
    for y in counter :
        if counter[y] != 0:
            return False

    return True

print(anagram2('dog','god'))
