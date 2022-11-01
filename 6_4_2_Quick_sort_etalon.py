from random import randint
from operator import itemgetter

def test():
	a = [randint(1, int(1e9)) for i in range(int(1e4))]
	# a = [randint(1, 10) for i in range(6)]
	quick_sort(a, 0, len(a))
	print(a)
	for i in range(1, len(a)):
		assert a[i] >= a[i-1]
	print('vse OK')


def quick_sort(lst: list, start: int, finish: int) -> list:
	# print(f'lst: {lst}, start: {start}, finish: {finish}')
	if finish - start > 1:
		center = partition(lst, start, finish)
		# print(f'quick_sort center: {center}')
		quick_sort(lst, start, center)
		quick_sort(lst, center+1, finish)
	return lst


def partition(lst: list, start: int, finish: int) -> int:
	# print(f'partition lst: {lst}, start: {start}, finish: {finish}')
	pivot = lst[finish-1]
	wall = 0
	for index in range(finish-1):
		# print('partition', lst)
		if lst[index] > pivot:
			# print('partition', lst[index], '>', pivot)
			continue
		else:
			# print('partition', lst[index], '<=', pivot)
			value_changer(lst, index, wall)
			wall += 1
	value_changer(lst, finish-1, wall)
	return wall
	

def value_changer(lst: list, index_1: int, index_2: int) -> list:
	value_1 = lst[index_1]
	lst[index_1] = lst[index_2]
	lst[index_2] = value_1

if __name__ == '__main__':
	test()

