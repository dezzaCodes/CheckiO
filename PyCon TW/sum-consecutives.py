def sum_consecutives(a):
	ans = []
	i = 0
	while i < len(a):
		j = i + 1
		if j < len(a) and a[i] == a[j]:
			multiply = 1
			while j < len(a) and a[i] == a[j]:
				multiply += 1
				j += 1
			sum = multiply * a[i]
			ans.append(sum)
			i = j
		else:
			ans.append(a[i])
			i += 1
	return ans


if __name__ == '__main__':
	print("Example:")
	print(list(sum_consecutives([1, 1, 1, 1])))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(sum_consecutives([1, 1, 1, 1])) == [4]
	assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
	assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
	assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
	assert list(sum_consecutives([1])) == [1]
	assert list(sum_consecutives([])) == []
	print("Coding complete? Click 'Check' to earn cool rewards!")
