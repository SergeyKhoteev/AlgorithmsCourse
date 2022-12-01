from _Generate_test_data import generate_quick_sort_data
from random import randint
from operator import itemgetter
from time import sleep, perf_counter
from sys import stdin


def timer(func):
	def _wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		runtime = perf_counter() - start
		print(f"{func.__name__} took {runtime:.4f} secs")
		return result
	return _wrapper


def prepare_data_main():
	reader = (list(map(int, line.split())) for line in stdin)
	lines_total, points_total = next(reader)
	lines = [next(reader) for i in range(lines_total)]
	startings = [line[0] for line in lines]
	endings = [line[1] for line in lines]
	points = next(reader)

	return startings, endings, points, lines, lines_total


def main():
	startings, endings, points, lines, lines_total = prepare_data_main()

	### Sorting lists ###
	quick_sort(array = startings, start = 0, finish = lines_total)
	quick_sort(array = endings, start = 0, finish = lines_total)

	### List quick_sort results verification ###
	# for i in range(1, len(startings)):
	# 	assert startings[i] >= startings[i - 1]
	# 	assert endings[i] >= endings[i - 1]

	### Calculating result for each point ###
	res_dict = {}
	print_str = ''
	for target in points:
		if target in res_dict:
			print_str += str(res_dict[target])
			print_str += ' '
		else:
			starting_boundary = find_starting_boundary_updated(
				array = startings,
				target = target)
			ending_boundary = find_ending_boundary_updated(
				array = endings,
				target = target)
			result = starting_boundary - ending_boundary
			res_dict[target] = result
			print_str += str(result)
			print_str += ' '

			### Naive way to calculate result and verify algorithm result ###
			
			# count = 0
			# for i in range(len(lines)):
			# 	if lines[i][0] <= target <= lines[i][1]:
			# 		count += 1
			# assert result == count, f'result = {result}, count = {count}, target = {target} \n {startings} \n {endings} \n {starting_boundary} {startings[starting_boundary]}, \n {ending_boundary} {endings[ending_boundary]}'
	
	print(print_str)


def quick_sort(array: list, start: int, finish: int):
	if finish > start:
		finish_1, start_2 = partition(array = array, start = start, finish = finish)
		quick_sort(array = array, start = start, finish = finish_1)
		quick_sort(array = array, start = start_2, finish = finish)


### Function sorts array in comparison to last value. Returns start and finish of the "wall"###
def partition(array: list, start: int, finish: int):
	pivot_index = find_array_median(array = array, start = start, finish = finish - 1)
	value_changer(array, pivot_index, finish - 1)
	pivot_index = finish - 1
	pivot = array[pivot_index]
	wall = start
	i = start
	while True:
		if i == pivot_index:
			break
		if array[i] == pivot:
			pivot_index -= 1
			value_changer(array, i, pivot_index)
			continue
		if array[i] > pivot:
			i += 1
			continue
		if array[i] < pivot:
			value_changer(array, i, wall)
			wall += 1
			i += 1
			continue
	start = wall
	for i in range(pivot_index, finish):
		value_changer(array, i, wall)
		wall += 1
	finish = wall
	return start, finish


def find_array_median(array: list, start: int, finish: int) -> int:
	lst = [
	[start, array[start]],
	[(start + finish) // 2, array[(start + finish) // 2]],
	[finish, array[finish]]]
	lst.sort(key=itemgetter(1))
	return lst[1][0]


### Function swaps values in array between 2 indexes ### 
def value_changer(array: list, index_1: int, index_2: int):
	value_1 = array[index_1]
	array[index_1] = array[index_2]
	array[index_2] = value_1


### Function to find target in array and return its index, otherwise it returns next nearest index
def binary_search(array: list, target: int) -> int:
	start = 0
	finish = len(array) - 1
	while finish - start >= 0:
		mid = (finish + start) // 2
		if array[mid] == target:
			return mid
		if array[mid] < target:
			start = mid + 1
			continue
		if array[mid] > target:
			finish = mid - 1
			continue
	if array[mid] > target:
		return mid
	if array[mid] < target:
		if mid == len(array) - 1:
			return mid
		return mid + 1


### Function to define boundary of startings array ###
def find_starting_boundary_updated(array: list, target: int) -> int:
	start = binary_search(array = array, target = target)
	if array[start] < target:
		return start + 1
	target_2 = target + 1
	finish = binary_search(array = array, target = target_2)
	target_2 = array[finish]
	if target_2 == target:
		return finish + 1
	while finish - start >= 0:
		mid = (finish + start) // 2
		if array[mid] == target:
			start = mid + 1
		if array[mid] == target_2:
			finish = mid - 1
	return start


### Same as "find_starting_boundary" but for endings
def find_ending_boundary_updated(array: list, target: int) -> int:
	target_2 = target - 1
	start = binary_search(array = array, target = target_2)
	if array[start] == target:
		return start
	target_2 == array[start]
	finish = binary_search(array = array, target = target)
	while finish - start > 0:
		mid = (finish + start) // 2
		if array[mid] == target_2:
			start = mid + 1
		if array[mid] == target:
			finish = mid - 1
	if array[start] >= target:
		return start
	else:
		return start + 1


if __name__ == '__main__':
	generate_quick_sort_data()
	main()		
