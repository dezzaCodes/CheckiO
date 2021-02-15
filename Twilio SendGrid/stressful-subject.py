def is_stressful(subj):
	"""
		recognize stressful subject
	"""

	if subj.isupper():
		return True

	dict = ["help", "asap", "urgent"]
	for word in dict:
		if word in removeDuplicateLetters(subj):
			return True

	if subj.endswith('!!!'):
		return True
	return False


def removeDuplicateLetters(word):
	word = word.lower()

	curr = ''
	ans = ''

	for letter in word:
		if letter.isalpha() and letter != curr:
			ans = ans + letter
			curr = letter
	return ans


if __name__ == '__main__':
	# These "asserts" are only for self-checking and not necessarily for auto-testing
	assert is_stressful("Hi") == False, "First"
	assert is_stressful("I neeed HELP") == True, "Second"
	print('Done! Go Check it!')
