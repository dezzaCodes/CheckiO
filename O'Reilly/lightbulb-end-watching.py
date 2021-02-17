from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
			  end_watching: Optional[datetime] = None) -> int:
	"""
		how long the light bulb has been turned on
	"""
	if not start_watching:
		start_watching = els[0]

	if not end_watching:
		end_watching = els[len(els) - 1]

	end_time = els[len(els) - 1] if els[len(els) - 1] > end_watching else end_watching

	if len(els) % 2 == 1:
		els.append(end_time)

	time = 0

	for i in range(0, len(els), 2):
		if els[i + 1] < start_watching or end_watching < els[i]:
			pass
		else:
			if els[i] < start_watching:
				els[i] = start_watching
			if end_watching < els[i + 1]:
				els[i + 1] = end_watching
			time = time + (els[i + 1] - els[i]).total_seconds()

	return time


if __name__ == '__main__':
	print("Example:")
	print(sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10)))

	assert sum_light(els=[
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
		start_watching=datetime(2015, 1, 12, 10, 0, 0),
		end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 7)) == 7

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
		datetime(2015, 1, 12, 10, 0, 3),
		datetime(2015, 1, 12, 10, 0, 10)) == 7

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
		datetime(2015, 1, 12, 10, 0, 10),
		datetime(2015, 1, 12, 10, 0, 20)) == 0

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 10, 30, 0),
		datetime(2015, 1, 12, 11, 0, 0)) == 0

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 10, 10, 0),
		datetime(2015, 1, 12, 11, 0, 0)) == 10

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 10, 10, 0),
		datetime(2015, 1, 12, 11, 0, 10)) == 20

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 9, 50, 0),
		datetime(2015, 1, 12, 10, 0, 10)) == 10

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 9, 0, 0),
		datetime(2015, 1, 12, 10, 5, 0)) == 300

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
		datetime(2015, 1, 12, 11, 5, 0),
		datetime(2015, 1, 12, 12, 0, 0)) == 310

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
		datetime(2015, 1, 12, 11, 5, 0),
		datetime(2015, 1, 12, 11, 10, 0)) == 300

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
		datetime(2015, 1, 12, 10, 10, 0),
		datetime(2015, 1, 12, 11, 0, 10)) == 20

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
		datetime(2015, 1, 12, 9, 10, 0),
		datetime(2015, 1, 12, 10, 20, 20)) == 610

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
		datetime(2015, 1, 12, 9, 10, 0),
		datetime(2015, 1, 12, 10, 20, 20)) == 1220

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
		datetime(2015, 1, 12, 9, 9, 0),
		datetime(2015, 1, 12, 10, 0, 0)) == 0

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
		datetime(2015, 1, 12, 9, 9, 0),
		datetime(2015, 1, 12, 10, 0, 10)) == 10

	print("The third mission in series is completed? Click 'Check' to earn cool rewards!")