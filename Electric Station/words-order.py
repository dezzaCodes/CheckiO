def words_order(text: str, words: list) -> bool:
	# your code here

	split = text.split()

	for word in words:
		if words.count(word) > 1:
			return False
		if word in split:
			split = split[split.index(word) + 1:]
		else:
			return False

	return True


if __name__ == '__main__':
	print("Example:")
	print(words_order('hi world im here', ['world', 'here']))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert words_order('hi world im here', ['world', 'here']) == True
	assert words_order('hi world im here', ['here', 'world']) == False
	assert words_order('hi world im here', ['world']) == True
	assert words_order('hi world im here',
					   ['world', 'here', 'hi']) == False
	assert words_order('hi world im here',
					   ['world', 'im', 'here']) == True
	assert words_order('hi world im here',
					   ['world', 'hi', 'here']) == False
	assert words_order('hi world im here', ['world', 'world']) == False
	assert words_order('hi world im here',
					   ['country', 'world']) == False
	assert words_order('hi world im here', ['wo', 'rld']) == False
	assert words_order('', ['world', 'here']) == False
	print("Coding complete? Click 'Check' to earn cool rewards!")
