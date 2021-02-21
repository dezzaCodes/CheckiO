def time_converter(time):
	# replace this for solution
	split = time.split(':')

	if int(split[0]) < 12:
		if split[0] == '00':
			split[0] = 12
		string = ' a.m.'
	else:
		if split[0] != '12':
			split[0] = int(split[0]) - 12
		string = ' p.m.'

	return str(int(split[0])) + ':' + split[1] + string


if __name__ == '__main__':
	print("Example:")
	print(time_converter('12:30'))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert time_converter('12:30') == '12:30 p.m.'
	assert time_converter('09:00') == '9:00 a.m.'
	assert time_converter('23:15') == '11:15 p.m.'
	print("Coding complete? Click 'Check' to earn cool rewards!")
