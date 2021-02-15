def is_all_upper(text: str) -> bool:
	# your code here
	if not text:
		return True

	return text.isupper() or text.isspace() or text.isnumeric()


if __name__ == '__main__':
	print("Example:")
	print(is_all_upper('ALL UPPER'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_all_upper('ALL UPPER') == True
	assert is_all_upper('all lower') == False
	assert is_all_upper('mixed UPPER and lower') == False
	assert is_all_upper('') == True
	assert is_all_upper('     ') == True
	print("Coding complete? Click 'Check' to earn cool rewards!")


# def is_all_upper(text):
#     return text == text.upper()