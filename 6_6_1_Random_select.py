from _Generate_test_data import generate_random_select_data
from sys import stdin
from time import sleep
from random import randint
from time import perf_counter


### Decorator to calculate function time consumption
def timer(func):
	def wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		finish = perf_counter()
		print(f'func {func.__name__} took {(finish - start):.5f}')
		return result
	return wrapper


### Main algorithm
@timer
def main():
	reader = (list(map(int, line.split())) for line in stdin)
	total = int(next(reader)[0])
	target_index = int(next(reader)[0])
	points = next(reader)

	value = random_select(array = points, start = 0, finish = total, target_index = target_index)
	print(value)


### Function to get quick_sort result, and compare time consumption vs random_search
@timer
def test():
	reader = (list(map(int, line.split())) for line in stdin)
	total = int(next(reader)[0])
	target_index = int(next(reader)[0])
	points = next(reader)

	quick_sort(array = points, start = 0, finish = total)
	print(points[target_index])


### Recursive funk to return value of target_index
def random_select(array: list, start: int, finish: int, target_index: int):
	if finish > start:
		starting, ending = partition(array = array, start = start, finish = finish)
		if target_index < starting:
			return random_select(array = array, start = start, finish = starting, target_index = target_index)
		if target_index > ending:
			return random_select(array = array, start = ending, finish = finish, target_index = target_index)
		else:
			return array[starting]


### Casual Quick_sort funktion with 3 intervals
def quick_sort(array: list, start: int, finish: int):
	if finish > start:
		starting, ending = partition(array = array, start = start, finish = finish)
		quick_sort(array = array, start = start, finish = starting)
		quick_sort(array = array, start = ending, finish = finish)


### Divides array and return starting and ending of random element
def partition(array:list, start:int, finish:int):
	if finish > start:
		pivot_index = randint(start, finish - 1)
		value_changer(array = array, index_1 = pivot_index, index_2 = finish - 1)
		pivot = array[finish - 1]
		wall_start = start
		wall_finish = finish - 1
		i = start

		while i < wall_finish:
			if array[i] < pivot:
				value_changer(array = array, index_1 = i, index_2 = wall_start)
				i += 1
				wall_start += 1
				continue
			if array[i] > pivot:
				i += 1
				continue
			if array[i] == pivot:
				wall_finish -= 1
				value_changer(array = array, index_1 = i, index_2 = wall_finish)
				continue

		starting = wall_start
		for i in range(wall_finish, finish):
			value_changer(array = array, index_1 = i, index_2 = wall_start)
			wall_start += 1
		ending = wall_start

		return starting, ending


### Func to swap values in array
def value_changer(array:list, index_1: int, index_2:int):
	value_1 = array[index_1]
	array[index_1] = array[index_2]
	array[index_2] = value_1


if __name__ == '__main__':
	generate_random_select_data()
	main()
