from _Generate_test_data import generate_lis_data
from sys import stdin


def main():
	reader = (line for line in stdin)
	limit = int(next(reader))
	array = list(map(int, next(reader).split()))
	lnis_last_values, predecessors, length = find_lnis(array = array, limit = limit)
	print(length)

	### Printing solution with the help of supportive arrays
	index = lnis_last_values[-1]
	value = array[index]
	indexes = ['x' for i in range(length)]
	values = ['x' for i in range(length)]
	indexes[-1] = index + 1
	values[-1] = value
	for i in range(length - 2, -1, -1):
		index = predecessors[index]
		value = array[index]
		indexes[i] = index + 1
		values[i] = value
	print(' '.join(list(map(str, values))))
	print(' '.join(list(map(str, indexes))))


### Difines LNIS with the help of 2 supportive arrays.
### Array Predecessors keeps indexes of child to each element
### Array Last_values keeps last indexes of LNIS of current i length
def find_lnis(array: list, limit: int):
	lnis_last_values = [0]
	predecessors = [-1 for i in range(limit)]
	length = 1
	for i in range(1, limit):

		if array[i] <= array[lnis_last_values[-1]]:
			predecessors[i] = lnis_last_values[-1]
			length += 1
			lnis_last_values.append(i)
			continue
		if array[i] > array[lnis_last_values[0]]:
			lnis_last_values[0] = i
			continue
		else:
			border = border_search(
				array = array, 
				lnis_last_values = lnis_last_values, 
				length = length,
				target = array[i])
			lnis_last_values[border] = i
			predecessors[i] = lnis_last_values[border - 1]

	return lnis_last_values, predecessors, length


### Finds the border between "target" and next item. Returns the "next to target" index
def border_search(array: list, lnis_last_values: list, length: int, target: int) -> int:
	start = 0
	finish = length - 1
	while finish != start:
		mid = (start + finish) // 2
		if array[lnis_last_values[mid]] == target:
			if mid == length - 1:
				return mid
			if array[lnis_last_values[mid + 1]] != target:
				return mid + 1
			else:
				start = mid + 1
			continue
		if array[lnis_last_values[mid]] > target:
			start = mid + 1
			continue
		if array[lnis_last_values[mid]] < target:
			finish = mid
			continue
	return finish


if __name__ == '__main__':
	generate_lis_data()
	main()
