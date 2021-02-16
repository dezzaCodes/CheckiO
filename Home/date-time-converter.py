def date_time(time: str) -> str:
	# replace this for solution
	months = ["Unknown",
			  "January",
			  "Febuary",
			  "March",
			  "April",
			  "May",
			  "June",
			  "July",
			  "August",
			  "September",
			  "October",
			  "November",
			  "December"]

	day = str(int(time[:2]))
	month = months[int(time[3:5])]
	year = str(int(time[6:10]))
	hour = str(int(time[11:13]))
	mins = str(int(time[14:16]))

	if hour == '1':
		hourString = ' hour '
	else:
		hourString = ' hours '

	if mins == '1':
		minString = ' minute'
	else:
		minString = ' minutes'

	return day + ' ' + month + ' ' + year + ' year ' + hour + hourString + mins + minString


if __name__ == '__main__':
	print("Example:")
	print(date_time('01.01.2000 00:00'))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
	assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
	assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
	print("Coding complete? Click 'Check' to earn cool rewards!")
