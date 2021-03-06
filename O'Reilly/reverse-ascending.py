def reverse_ascending(items):
	# your code here

	ans = []
	lower = 0

	for i in range(0, len(items) - 1):
		if items[i] >= items[i + 1]:
			upper = i + 1
			print(upper)
			print(lower)
			ans = ans + sorted(items[lower:upper], reverse=True)
			lower = i + 1
	upper = len(items)
	ans = ans + sorted(items[lower:upper], reverse=True)
	return ans


if __name__ == '__main__':
	print("Example:")
	print(reverse_ascending([1, 2, 3, 4, 5]))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
	assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
	assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
	assert list(reverse_ascending([])) == []
	assert list(reverse_ascending([1])) == [1]
	assert list(reverse_ascending([1, 1])) == [1, 1]
	assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
	print("Coding complete? Click 'Check' to earn cool rewards!")
