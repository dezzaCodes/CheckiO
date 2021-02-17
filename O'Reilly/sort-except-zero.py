from typing import Iterable


def except_zero(items: list) -> Iterable:
	# your code here

	non_zero = []
	for num in items:
		if num != 0:
			non_zero.append(num)

	non_zero = sorted(non_zero)
	print(non_zero)

	j = 0
	ans = []
	for num in items:
		if num == 0:
			ans.append(0)
		else:
			ans.append(non_zero[j])
			j = j + 1

	return ans


if __name__ == '__main__':
	print("Example:")
	print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
	assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
	assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
	assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
	assert list(except_zero([0, 0])) == [0, 0]
	print("Coding complete? Click 'Check' to earn cool rewards!")
