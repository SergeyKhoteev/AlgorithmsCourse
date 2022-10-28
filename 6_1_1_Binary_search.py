import sys
from random import randint
from time import sleep


def main():
	array = tuple(map(int, input().split()))[1:]
	elements = tuple(map(int, input().split()))[1:]
	for i in elements:
			print(finder(array, i), end=' ')

def finder(array: tuple, element: int) -> int:
	start = 0
	finish = len(array) - 1
	while finish - start != 1:
		middle = int(start + (finish - start) / 2)
		if array[middle] == element:
			return middle + 1
		elif array[middle] > element:
			finish = middle
			continue
		elif array[middle] < element:
			start = middle
			continue
	if element == array[start]:
		return start + 1
	elif element == array[finish]:
		return finish + 1
	else:
		return -1



def test():
	array = tuple(randint(1, 1e9) for i in range(randint(1, 1e5)))
	elements = tuple(randint(1, 1e9) for i in range(randint(1, 1e5)))
	# array = (1, 5, 8, 12, 13, 14)
	# elements = (8, 1, 23, 1, 11)
	for i in elements:
		print(finder(array, i), end=' ')

if __name__ == '__main__':
	# main()
	test()

