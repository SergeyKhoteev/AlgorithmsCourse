from sys import stdin
from _Generate_test_data import generate_lis_data


def main():
	reader = (line for line in stdin)
	limit = int(next(reader))
	array = list(map(int, next(reader).split()))
	sub_length, lnis_indexes = find_lnis(array = array, limit = limit)
	length, indexes = find_answer(sub_length = sub_length, lnis_indexes = lnis_indexes, limit = limit)
	print(length)
	print(' '.join(list(map(str, indexes))))


### Iteration of array in ascending order with subiteration of lis_array in descending order
### For each item in array length of Longest Not Increasing Subsequence is defined
def find_lnis(array: list, limit: int) -> tuple:
	sub_length = [1 for i in range(limit)]
	lnis_indexes = [-1 for i in range(limit)]
	for array_index in range(1, limit):
		for sub_length_index in range(array_index - 1, -1, -1):
			if array[array_index] <= array[sub_length_index] and sub_length[array_index] < (sub_length[sub_length_index] + 1):
				sub_length[array_index] = sub_length[sub_length_index] + 1
				lnis_indexes[array_index] = sub_length_index
	return sub_length, lnis_indexes


### Restores solution from lis array
def find_answer(sub_length: list, lnis_indexes: list, limit: int) -> tuple:
	length = 1
	max_index = 0
	for i in range(limit):
		if sub_length[i] > length:
			length = sub_length[i]
			max_index = i
	indexes = ['x' for i in range(length)]
	indexes[length - 1] = max_index + 1
	for i in range(length - 2, -1, -1):
		max_index = lnis_indexes[max_index]
		indexes[i] = max_index + 1
	return length, indexes


if __name__ == '__main__':
	generate_lis_data()
	main()
