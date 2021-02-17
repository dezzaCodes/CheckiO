def isometric_strings(str1: str, str2: str) -> bool:
	# your code here

	for i in range(0, len(str1)):
		if str1.count(str1[i]) != str2.count(str2[i]):
			return False
	return True


if __name__ == '__main__':
	print("Example:")
	print(isometric_strings('add', 'egg'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert isometric_strings('add', 'egg') == True
	assert isometric_strings('foo', 'bar') == False
	assert isometric_strings('', '') == True
	assert isometric_strings('all', 'all') == True
	print("Coding complete? Click 'Check' to earn cool rewards!")
