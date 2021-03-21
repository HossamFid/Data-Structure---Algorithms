# given array output all uniue pairs that sum up to a specific value


def pair_sum(lst,value):

	if len(lst) < 2 :
		return


	# sets for tracking
	seen = set()
	result = set()

	for num in lst :
		target = value - num



		if target not in seen :
			seen.add(num)
			print(seen)

		else :
			result.add((min(target,num), max(target,num)))
			print(result)
	print('\n'.join(map(str,list(result))))

print(pair_sum([1,3,2,2],4))
