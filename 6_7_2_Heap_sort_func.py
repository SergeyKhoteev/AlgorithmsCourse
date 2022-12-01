from sys import stdin
from _Generate_test_data import generate_heap_sort_data


### Takes array and bring it to heap_max. Vrifies result
def build_heap_max(array:list, limit: int):
	for parent_index in range(limit // 2, 0, -1):
		sift_down(array = array, parent_index = parent_index, limit = limit)
	assert_heap(array = array, limit = limit)


### Compares parent and its children. Swaps parent with biggest child
def sift_down(array: list, parent_index: int, limit:int):
	while parent_index <= limit:
		child_1_index = parent_index * 2
		if child_1_index <= limit:
			parent = array[parent_index]
			child_1 = array[child_1_index]
			child_2_index = child_1_index + 1 
			if child_2_index <= limit:
				child_2 = array[child_2_index]
				if parent >= child_1 and parent >= child_2:
					break
				if parent <= child_1 and parent <= child_2:
					if child_1 <= child_2:
						changer(array = array, index_1 = parent_index, index_2 = child_2_index)
						parent_index = child_2_index
						continue
					else:
						changer(array = array, index_1 = parent_index, index_2 = child_1_index)
						parent_index = child_1_index
						continue
				if parent <= child_2:
					changer(array = array, index_1 = parent_index, index_2 = child_2_index)
					parent_index = child_2_index
					continue
				if parent <= child_1:
					changer(array = array, index_1 = parent_index, index_2 = child_1_index)
					parent_index = child_1_index
					continue
			if parent <= child_1:
				changer(array = array, index_1 = parent_index, index_2 = child_1_index)
				break
			else:
				break
		else:
			break


### Vrifies array by comparing array item with its predecessor
def assert_array(array: list, limit: int):
	for i in range(2, limit):
		assert array[i] >= array[i - 1]
	print('array is ok')


### Takes heap_max and bring it to sorted list
def heap_sort(array: list, limit: int):
	build_heap_max(array = array, limit = limit)
	for index in range(limit, 1, -1):
		changer(array = array, index_1 = 1, index_2 = index)
		sift_down(array = array, parent_index = 1, limit = index - 1)
	assert_array(array = array, limit = limit)
	del array[0]


### Verifies heap_max and confirms its main rule
def assert_heap(array:list, limit: int):
	for i in range(1, limit):
		if i * 2 <= limit:
			assert array[i] >= array [i * 2], f'{array[i]} not <= {array [i * 2]}'
		if i * 2 + 1 <= limit:
			assert array[i] >= array[i * 2 + 1], f'{array[i]} not <= {array[i * 2 + 1]}' 
	print('heap is ok')


### Swaps list's items
def changer(array: list, index_1: int, index_2: int):
	value_1 = array[index_1]
	array[index_1] = array[index_2]
	array[index_2] = value_1


### Main algorithm
def main():
	reader = (list(map(int, line.split())) for line in stdin)
	limit = (next(reader))[0]
	array = [limit, *next(reader)]
	heap_sort(array = array, limit = limit)
	for i in range(1, len(array)):
		assert array[i] >= array[i -1]
	print('done')

if __name__ == '__main__':
	generate_heap_sort_data()
	main()
