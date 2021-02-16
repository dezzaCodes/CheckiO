def sun_angle(time):
	# replace this for solution

	hour = int(time[:2])
	mins = int(time[3:])

	if hour < 6 or hour > 18 or (hour == 18 and mins > 0):
		return "I don't see the sun!"
	return (hour - 6) * 15 + mins * .25


if __name__ == '__main__':
	print("Example:")
	print(sun_angle("07:00"))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert sun_angle("07:00") == 15
	assert sun_angle("01:23") == "I don't see the sun!"
	print("Coding complete? Click 'Check' to earn cool rewards!")
