import math
from typing import List, Tuple

Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
	x1 = (coords_1[0][0])
	x2 = (coords_1[1][0])
	x3 = (coords_1[2][0])

	y1 = (coords_1[0][1])
	y2 = (coords_1[1][1])
	y3 = (coords_1[2][1])

	side1 = math.sqrt(abs((y2 - y1) ** 2 + (x2 - x1) ** 2))
	side2 = math.sqrt(abs((y3 - y1) ** 2 + (x3 - x1) ** 2))
	side3 = math.sqrt(abs((y3 - y2) ** 2 + (x3 - x2) ** 2))

	tri1 = []
	tri1.append(side1)
	tri1.append(side2)
	tri1.append(side3)

	tri1 = sorted(tri1)

	x1 = (coords_2[0][0])
	x2 = (coords_2[1][0])
	x3 = (coords_2[2][0])

	y1 = (coords_2[0][1])
	y2 = (coords_2[1][1])
	y3 = (coords_2[2][1])

	side1 = math.sqrt(abs((y2 - y1) ** 2 + (x2 - x1) ** 2))
	side2 = math.sqrt(abs((y3 - y1) ** 2 + (x3 - x1) ** 2))
	side3 = math.sqrt(abs((y3 - y2) ** 2 + (x3 - x2) ** 2))

	tri2 = []
	tri2.append(side1)
	tri2.append(side2)
	tri2.append(side3)

	tri2 = sorted(tri2)

	ratio = tri1[0] / tri2[0]
	for i in range(1, 2):
		if ratio != tri1[i] / tri2[i]:
			return False
	return True


if __name__ == '__main__':
	print("Example:")
	print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
	assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
	assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
	assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
	print("Coding complete? Click 'Check' to earn cool rewards!")
