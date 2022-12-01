from _Generate_test_data import generate_count_sort_data
from sys import stdin

def main():
	reader = (line for line in stdin)
	limit = int(next(reader))
	array = list(map(int, next(reader).split()))
	array_sorted = count_sort(array = array, limit = limit)
	print(' '.join(list(map(str, array_sorted))))


def count_sort(array: list, limit: int):
	### Declaration how many different numbers is given in our array
	helper = [0 for i in range(11)]
	### Creation of empty list where sorted values will be kept
	sorted_list = [0 for i in range(limit)]
	### Iteration of the array and calculation sum of unique numbers
	for i in array:
		helper[i] += 1
	### Definition of 'last' index of every unique number in ascending order
	for i in range(2, 11):
		helper[i] = helper[i] + helper[i - 1]
	### Iteration of sorted array and storing the sorted values
	for i in range(limit - 1, -1, -1):
		sorted_list[helper[array[i]] - 1] = array[i]
		helper[array[i]] -= 1

	### Naive checker for sorted list
	# for i in range(1, limit):
		# assert sorted_list[i] >= sorted_list[i - 1]
	return sorted_list

if __name__ == '__main__':
	generate_count_sort_data()
	main()
