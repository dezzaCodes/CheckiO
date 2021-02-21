def checkio(line1: str, line2: str) -> str:
	# your code here
	split1 = line1.split(',')
	split2 = line2.split(',')

	ans = []
	for word in split1:
		if word in split2:
			ans.append(word)

	ans = sorted(ans)

	string = ''
	for word in ans:
		string += word + ','
	return string[:-1]


if __name__ == '__main__':
	print("Example:")
	print(checkio('hello,world', 'hello,earth'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert checkio('hello,world', 'hello,earth') == 'hello'
	assert checkio('one,two,three', 'four,five,six') == ''
	assert checkio('one,two,three',
				   'four,five,one,two,six,three') == 'one,three,two'
	print("Coding complete? Click 'Check' to earn cool rewards!")
