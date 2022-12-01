from _Generate_test_data import generate_lis_data
from sys import stdin


def main():
	reader = (line for line in stdin)
	limit = int(next(reader))
	array = list(map(int, next(reader).split()))
	lis_list = find_lis_BU(array = array, limit = limit)
	print(max(lis_list))


### Iteration of array in ascending order with subiteration of lis_array in descending order
### For each item in array length of Longest Multiple Subsequence is defined
def find_lis_BU(array: list, limit: int) -> list:
	lis_list = [1 for i in range(limit)]
	for i in range(1, limit):
		for j in range(i - 1, -1, -1):
			if lis_list[j] + 1 > lis_list[i] and array[i] % array[j] == 0:
				lis_list[i] = lis_list[j] + 1
	return lis_list


### Restores solution from lis array
def print_lis(lis_list: list, array: list, limit: int):
	lis = 0
	for i in range(limit):
		if lis_list[i] > lis:
			lis = lis_list[i]
			lis_index = i
	subsequence = ['x' for i in range(lis)]
	subsequence[lis - 1] = array[lis_index]
	for i in range(lis - 2, 0 - 1, -1):
		for j in range(lis_index - 1, -1, -1):
			if lis_list[j] == i + 1:
				if subsequence[i + 1] >= array[j]:
					if subsequence[i + 1] % array[j] == 0:
						lis_index = j
						subsequence[i] = array[j]
						break
	return subsequence


if __name__ == '__main__':
	generate_lis_data()
	main()
