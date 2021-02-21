def from_camel_case(name):
	# replace this for solution
	name = name[0].lower() + name[1:]

	ans = ''
	for letter in name:
		if letter.isupper():
			ans += '_' + letter.lower()
		else:
			ans += letter

	return ans


if __name__ == '__main__':
	print("Example:")
	print(from_camel_case("Name"))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert from_camel_case("MyFunctionName") == "my_function_name"
	assert from_camel_case("IPhone") == "i_phone"
	assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
	assert from_camel_case("Name") == "name"
	print("Coding complete? Click 'Check' to earn cool rewards!")