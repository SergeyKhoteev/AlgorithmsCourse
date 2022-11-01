from random import randint
from time import sleep


def test():
	array = [[randint(1, 1e8), randint(1, 1e8)] for i in range(50000)]
	targets = [randint(1, 50000) for i in range(50000)]
	quick_sort(array = array, start = 0, finish = (len(array) - 1), index = 0)
	for target in targets:
		print(f'target = {target}')
		search_list = array[0: binary_search_startings(array, target) + 1]
		quick_sort(array = search_list, start = 0, finish = (len(search_list) - 1), index = 1)
		# print(search_list)
		res1 = binary_search_endings(search_list, target)
		# print(f'res1 = {res1}')
		result_list = search_list[res1:]
		# print(result_list)
		# for i in result_list:
		# 	assert i[0] <= target <= i[1], f'{i}'
		result = len(result_list)
		print(result)
		count = 0
		assert_list = []
		for i in range(len(array)):
			if array[i][0] <= target and array[i][1] >= target:
				count += 1
		# 		assert_list.append(array[i])
		# for i in assert_list:
		# 	if i not in result_list:
		# 		print(f'{i} not found')

		assert count == result, f'{count} != {result}, \n \n {assert_list}, \n \n {search_list}, \n \n {result_list}, '
		print('ok')


def quick_sort(array: list, start:int, finish: int, index: int):
	if finish > start:
		wall = partition(array, start, finish, index)
		quick_sort(array, start, wall - 1, index)
		quick_sort(array, wall + 1, finish, index)


def partition(array: list, start: int, finish: int, index: int) -> int:
	pivot = array[finish][index]
	wall = start
	for i in range(start, finish):
		if array[i][index] > pivot:
			continue
		else:
			value_changer(array, i, wall)
			wall += 1
	value_changer(array, wall, finish)
	return wall


def value_changer(array: list, index_1: int, index_2: int):
	value = array[index_1]
	array[index_1] = array[index_2]
	array[index_2] = value


def binary_search_startings(array: list, target: int) -> int:
	start = 0
	finish = len(array) - 1
	while finish - start > 1:
		mid = (finish + start) // 2
		if array[mid][0] == target:
			while array[mid][0] == target:
				mid += 1
			return mid - 1
		elif array[mid][0] < target:
			start = mid
		elif array[mid][0] > target:
			finish = mid
	return start


def binary_search_endings(array: list, target: int):
	start = 0
	finish = len(array) - 1
	while finish - start > 1:	
		mid = (start + finish) // 2
		if array[mid][1] == target:
			while array[mid][1] == target:
				mid -= 1
			print(f'return mid {mid+1}')
			return mid + 1
		elif array[mid][1] < target:
			start = mid
		elif array[mid][1] > target:
			finish = mid
	if array[start][0] <= target <= array[start][1]:
		return start
	return finish


if __name__ == '__main__':
	test()

