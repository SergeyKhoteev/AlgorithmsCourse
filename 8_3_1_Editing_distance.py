from _Generate_test_data import generate_editing_data
from sys import stdin
from time import perf_counter


def timer(func):
	def wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		finish = perf_counter() - start 
		print(f'{finish:.5f}')
		return result
	return wrapper


# @timer
def main():
	reader = (line.strip() for line in stdin)
	global words
	words = list(reader)
	# words = ['editing', 'distance']
	print(*words, sep = '\n')
	len_1 = len(words[0])
	len_2 = len(words[1])
	storage = [[j if i == 0 else i if j == 0 else'x' for i in range(len_1 + 1)] for j in range(len_2 + 1)]
	distance = get_editing_distance_TD(storage = storage, x = len_1, y = len_2)
	print(distance)
	# print(storage)
	storage = [[j if i == 0 else i if j == 0 else'x' for i in range(len_1 + 1)] for j in range(len_2 + 1)]
	distance = get_editing_distance_BU(storage = storage, x = len_1, y = len_2)
	# print(storage)
	print(distance)


def get_editing_distance_TD(storage: list, x: int, y:int , ):
	if storage[y][x] != 'x':
		return storage[y][x]
	else:
		deletion = get_editing_distance_TD(storage, x - 1, y) + 1
		insertion = get_editing_distance_TD(storage, x, y - 1) + 1
		editing = get_editing_distance_TD(storage, x - 1, y - 1) + diff(x, y)
		storage[y][x] = min(
			deletion,
			insertion,
			editing)
		return storage [y][x]


def diff(x: int, y: int):
	if words[0][x - 1] == words[1][y - 1]:
		return 0
	else:
		return 1


def get_editing_distance_BU(storage: list, x: int, y: int):
	for i in range(1, y + 1):
		for j in range(1, x + 1):
			if words[0][j - 1] == words[1][i - 1]:
				diff = 0
			else:
				diff = 1
			storage[i][j] = min(
				storage[i - 1][j] + 1,
				storage[i][j - 1] + 1,
				storage[i - 1][j - 1] + diff)

	return storage[y][x]

if __name__ == '__main__':
	generate_editing_data()
	main()
